import React, { useState } from "react";

export default function ImageUploadForm() {
    const [files, setFiles] = useState({})

    const handleFileChange = (e) => {
        setFiles({ ...files, [e.target.name]: e.target.files[0] })
    }

    const handleSubmit = async(e) => {
        e.preventDefault()
        const formData = new FormData()
        Object.keys(files).forEach((key) => {
            formData.append(key, files[key])
        })

        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        })

        const result = await response.json()
        console.log(result)
    }

    return (
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
            <div>
                <label>Top View: <input type="file" name="top" onChange={handleFileChange} /></label>
            </div>
            <button type="submit">Upload</button>
        </form>
    );
}