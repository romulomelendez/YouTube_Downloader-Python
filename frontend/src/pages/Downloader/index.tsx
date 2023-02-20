import { useState } from "react"

import axios from "axios"

export const Downloader: React.FC = () => {

    type StreamProps = {
        itag: number,
        mime_type: string,
        resolution: string | number,
        fps: number,
        video_type: string,
    }

    type VideoProps = {
        title: string,
        thumbnail: string,
        streams: StreamProps[]
    }

    const [videoUrl, setVideoUrl] = useState("")
    const [video, setVideo] = useState<VideoProps>()

    const handleStream = (stream: StreamProps) => console.log(stream)

    const getVideoData = async () => {
        
        const videoDataResponse = await axios.post(import.meta.env.VITE_APP_API_URL, {
            "videoUrl": videoUrl
        })

        setVideo({
            title: videoDataResponse.data.title,
            thumbnail: videoDataResponse.data.thumbnail_url,
            streams: videoDataResponse.data.streams
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
                        {
                            video.streams.map((stream: StreamProps, index: number) => (
                                <div key={index} onClick={() => handleStream(stream)}>
                                    <p>ITAG: { stream.itag }</p>
                                    <p>MIME TYPE: { stream.mime_type }</p>
                                    <p>RESOLUTION: { stream.resolution }</p>
                                    <p>FPS: { stream.fps }</p>
                                    <p>VIDEO TYPE: { stream.video_type }</p>
                                </div>
                            ))
                        }
                    </>
                : <p>Nothing to show!</p>
            }

        </>
    )
}