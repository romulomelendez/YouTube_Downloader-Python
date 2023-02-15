import { useState } from "react"

import axios from "axios"

export const Downloader: React.FC = () => {

    const [videoUrl, setVideoUrl] = useState("")

    const getVideoData = async () => {
        
        const videoResponse = await axios.post("http://localhost:5000", {
            "videoUrl": videoUrl
        })

        console.log(videoResponse)
    }

    return (
        <form>
            <input type="text" onChange={e => setVideoUrl(e.target.value)} />
            <button type="button" onClick={getVideoData}>Download</button>
        </form>
    )
}