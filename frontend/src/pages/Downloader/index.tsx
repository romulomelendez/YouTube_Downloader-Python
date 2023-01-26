export const Downloader: React.FC = () => {

    return (
        <form action="http://localhost:5000/" method="POST">
            <input type="text" name="video_url" />
            <button type="submit">Download</button>
        </form>
    )
}