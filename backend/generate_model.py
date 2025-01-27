import bpy
import sys
import os

# Parse arguments from the command line
args = sys.argv[sys.argv.index('--') + 1:]
file_paths = {arg.split(':')[0]: arg.split(':')[1] for arg in args}

# Debug: Print file paths
print(f"File paths: {file_paths}")
for side, filepath in file_paths.items():
    if not os.path.exists(filepath):
        print(f"Missing file for {side}: {filepath}")

# Clear all objects in the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create a cube (simplified model of the car body)
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
cube = bpy.context.object
cube.scale = (2.5, 1.0, 1.0)

# Create materials and assign textures to them
materials = {}
for side, filepath in file_paths.items():
    mat = bpy.data.materials.new(name=f'{side}_Material')
    mat.use_nodes = True

    texture_node = mat.node_tree.nodes.new(type='ShaderNodeTexImage')
    texture_node.image = bpy.data.images.load(filepath=filepath)

    bsdf_node = mat.node_tree.nodes["Principled BSDF"]
    mat.node_tree.links.new(texture_node.outputs["Color"], bsdf_node.inputs["Base Color"])

    materials[side] = mat

# Map materials to specific cube faces
face_material_map = {
    'front': 1,  # Front face
    'back': 3,   # Back face
    'left': 0,   # Left face
    'right': 2,  # Right face
}

# Debug: Assign materials to cube faces
print("Assigning materials to faces...")
for side, face_index in face_material_map.items():
    if side in materials:
        # Add material to the object
        cube.data.materials.append(materials[side])
        # Assign material to the specific face
        cube.data.polygons[face_index].material_index = len(cube.data.materials) - 1
        print(f"Assigned {side} material to face {face_index}")
    else:
        print(f"Material for {side} not found.")

# Define the output directory and file path
output_dir = os.path.abspath(os.path.join(os.getcwd(), "../backend", "generated_models"))
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'generated_model.gltf')

# Export the cube as a GLTF file
try:
    bpy.ops.export_scene.gltf(
        filepath=output_path,
        use_selection=True  # Export only selected objects
    )
    print(f'Model successfully exported to {output_path}')
except Exception as e:
    print(f'Export failed: {e}')
