import { useState } from "react"

import axios from "axios"

export const Downloader: React.FC = () => {

    type StreamProps = {
        itag: number,
        mime_type: string,
        resolution: string,
        fps: number,
        video_type: string,
    }

    type VideoProps = {
        title: string,
        thumbnail: string,
        streams: StreamProps[]
    }

    const [videoUrl, setVideoUrl] = useState("")
    const [streamSelected, setStreamSelected] = useState("")
    const [video, setVideo] = useState<VideoProps>()

    const handleStream = async () => {
        const downloadResponse = await axios.get(import.meta.env.VITE_APP_API_URL + `/download/${streamSelected}`)
    }

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
                <input type="text" onChange={ e => setVideoUrl(e.target.value) } />
                <button type="button" onClick={ getVideoData }>Download</button>
            </form>

            {
                video ?
                    <>
                        <h1>{ video.title }</h1>
                        <img src={ video.thumbnail } alt="thumbnail video" width="80" height="80" />
                        <select name={streamSelected} onChange={e => setStreamSelected(e.target.value)}>
                            {
                                video.streams.map((stream: StreamProps, index: number) => (
                                    <option value={ stream.itag } key={ index }>
                                        RESOLUTION: { stream.resolution } | FPS: { stream.fps } | MIME TYPE: { stream.mime_type }
                                    </option>
                                ))
                            }
                        </select>
                        <button type="button" onClick={ handleStream }>Download Video</button>
                    </>
                : <p>Nothing to show!</p>
            }

        </>
    )
}