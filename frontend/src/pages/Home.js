import React from "react";
import ImageUploadForm from "../components/ImageUploadForm";

export default function Home() {
    return (
        <div className="home-page">
            <h1>Home Page</h1>
            <h2>Upload 5 pictures of your car please</h2>
            <div className="img-upload-cont">
                <ImageUploadForm />
            </div>
        </div>
    )
}