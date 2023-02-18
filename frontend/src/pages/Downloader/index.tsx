import { useState } from "react"

import axios from "axios"

export const Downloader: React.FC = () => {

    type VideoProps = {
        title: string,
        thumbnail: string
    }

    const [videoUrl, setVideoUrl] = useState("")
    const [video, setVideo] = useState<VideoProps>()

    const getVideoData = async () => {
        
        const videoDataResponse = await axios.post(import.meta.env.VITE_APP_API_URL, {
            "videoUrl": videoUrl
        })

        setVideo({
            title: videoDataResponse.data.title,
            thumbnail: videoDataResponse.data.thumbnail_url
        })
    }

    return (
        <>
            <form>
                <input type="text" onChange={e => setVideoUrl(e.target.value)} />
                <button type="button" onClick={getVideoData}>Download</button>
            </form>

            {
                video ?
                    <>
                        <h1>{video.title}</h1>
                        <img src={video.thumbnail} alt="thumbnail video" width="80" height="80" />
                    </>
                : <p>Nothing to show!</p>
            }

        </>
    )
}