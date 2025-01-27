import React, { useState } from "react";

export default function ImageUploadForm() {
    const [files, setFiles] = useState({})
    const [message, setMessage] = useState('')
    const [model, setModel] = useState(null)

    const handleFileChange = (e) => {
        setFiles({ ...files, [e.target.name]: e.target.files[0] })
    }

    const handleSubmit = async(e) => {
        e.preventDefault()

        const requiredFiles = ['front', 'left', 'right', 'back']
        // const requiredFiles = ['front']
        const missingFiles = requiredFiles.filter((key) => !files[key])
        
        if (missingFiles.length > 0) {
            setMessage(`Missing files: ${missingFiles.join(", ")}`)
            return
        }

        const formData = new FormData()
        Object.keys(files).forEach((key) => {
            formData.append(key, files[key])
        })

        try {
            const response = await fetch('http://127.0.0.1:5000/upload', {
                method: 'POST',
                body: formData
            })

            const result = await response.json()

            if (response.ok) {
                setMessage("Files uploaded and processed successfully.")
                setModel(result.processed_files)
                console.log(result)
            } else {
                setMessage(`Error: ${result.error || "Unknown error occurred"}`)
            }
        } catch (error) {
            setMessage("An error occurred while uploading the files.")
            console.error(error)
        }
    }

    const handleGenerateModel = async() => {
        try {
            const response = await fetch('http://127.0.0.1:5000/generate-model', {
                method:'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body: JSON.stringify({processed_files:model})
            })

            const result = await response.json()

            if (response.ok) {
                setMessage('3D model generated successfully')
                console.log(result.model_path)
            } else {
                setMessage(`Error: ${result.error || "Unknown error occurred."}`)
            }
        } catch (error) {
            setMessage("An error occurred while generating the model.")
            console.error(error)
        }
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Front View: <input type="file" name="front" onChange={handleFileChange} /></label>
                </div>
                <div>
                    <label>Left Side View: <input type="file" name="left" onChange={handleFileChange} /></label>
                </div>
                <div>
                    <label>Right Side View: <input type="file" name="right" onChange={handleFileChange} /></label>
                </div>
                <div>
                    <label>Back View: <input type="file" name="back" onChange={handleFileChange} /></label>
                </div>
                <button type="submit">Upload</button>
            </form>
            {message && <p>{message}</p>}
            <button
                onClick={handleGenerateModel}
                disabled={!model}
                style={{
                    backgroundColor: !model && '#CCCCCC',
                    cursor: model ? 'pointer' : 'not-allowed',
                }}
            >
                Generate Model
            </button>
        </div>
    )
}