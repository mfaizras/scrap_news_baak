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
    discord = Discord()


main()
