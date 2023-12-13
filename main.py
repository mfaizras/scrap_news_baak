from News import News
from Discord import Discord


def split_content(content, chunk_size=3950):
    # Check if content length is greater than or equal to the specified chunk size
    if len(content) >= chunk_size:
        # Find the index to split at the last space before the chunk size
        last_space_index = content.rfind(" ", 0, chunk_size)

        # If no space is found, split at the chunk size
        split_index = last_space_index if last_space_index != -1 else chunk_size

        # Split the content at the determined index
        chunk = content[:split_index]

        # Recursively call the function for the remaining content
        remaining_chunks = split_content(content[split_index:].lstrip(), chunk_size)

        # Combine the current chunk with the remaining chunks
        return [chunk] + remaining_chunks
    else:
        # If the content is less than the specified chunk size, return the original content
        return [content]


def main():
    news = News()
    news_list = news.get_data_news()

    new_berita = "==== New Beritaaaa BAAK ====\n"
    for new in news_list:
        new_detail = news.get_new_by_id(new.id)
        results_chunk = split_content(content=new_detail.body)
        # Print or use the resulting chunks as needed

        body_msg = ""
        for i, chunk in enumerate(results_chunk):
            body_msg += chunk

        new_berita += (
            f"```{new.title}\n{new.date}```" + "\n" + f"```{body_msg}```" + "\n\n"
        )

    discord = Discord()
    result = discord.send_message(1182984217425088552, new_berita)
    print(result)


main()
