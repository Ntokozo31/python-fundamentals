"""
This program Start with:  
`["Song A", "Song C"]`  
Using only `insert` and `append`/`extend`, make the final playlist become:  
`["Song A", "Song B", "Song C", "Song D", "Song E"]`  
Print the playlist after each modification.
"""


playlist = ["Song A", "Song C"]

playlist.insert(1, "Song B")
print(playlist)

playlist.extend(["Song D", "Song E"])
print(playlist)