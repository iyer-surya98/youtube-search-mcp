from youtube_search import YoutubeSearch
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("youtube-search")


@mcp.tool()
def search_for_youtube_videos(query: str):
    search = YoutubeSearch(search_terms=query, max_results=10)
    return {
        "videos": [
            {
                k: v
                for k, v in video_obj.items()
                if k not in ["thumbnails", "long_desc", "url_suffix"]
            }
            for video_obj in search.to_dict()
        ]
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
