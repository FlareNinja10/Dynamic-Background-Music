from serpent import *

# This map links the Game Layer to the song file in your resources
# Make sure the filenames match your uploaded mp3s exactly!
MUSIC_MAP = {
    "MenuLayer": "main_menu.mp3",
    "CreatorLayer": "editor_vibes.mp3",
    "LevelInfoLayer": "lobby.mp3",
    "LevelBrowserLayer": "browser_music.mp3"
}

@hook(CCLayer, "onEnter")
def on_layer_enter(self):
    # Let the game load the screen normally first
    self.original()
    
    # Get the name of the screen the player just entered
    layer_name = self.get_class_name()
    
    # If the screen is in our map, play the song
    if layer_name in MUSIC_MAP:
        song_name = MUSIC_MAP[layer_name]
        
        # We use Geode's sound manager to play the file from our mod resources
        # 'self' refers to the current mod instance in Serpent
        GameManager.sharedState().fadeInMusic(song_name)

print("DBM Mod Loaded Successfully!")
