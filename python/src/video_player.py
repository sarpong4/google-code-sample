"""A video player class."""

from .video_library import VideoLibrary
import random


# Open videos file and parse each line as a list
videos = []
with open('src/videos.txt') as f:
    videos = f.read().splitlines()

# dictionary sets current playing status of all videos to 0 (not playing) - currently playing = 1
current_play = {}

# dictionary that relates vide0_id to video
video = {}
required_video = {}
show_playingVid = {} # dictionary to relate video_id to line of videos.txt
for v in videos:
    v_tagout = v.split(' |  ')
    if len(v_tagout) >= 2:
        x = v_tagout[0].split(' | ')
        video[x[1]] = x[0]
        current_play[x[0]] = 0
        required_video[x[1]] = 0 # to use in show_playing. id equivalent of current_play
        show_playingVid[x[1]] = v
    else:
        x = v_tagout[0].split(' | ')
        y = x[1].split(' |')
        video[y[0]] = x[0]
        current_play[x[0]] = 0
        required_video[y[0]] = 0 # to use in show_playing. id equivalent of current_play
        show_playingVid[y[0]] = v

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.videos = videos
        self.video = video
        self.current_play = current_play
        self.show_playingVid = show_playingVid
        self.required_video = required_video

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        split_videos = []
        for view in sorted(self.videos):
            vid_dec = view.split(' |  ')
            split_videos.append(vid_dec)

        for desc in split_videos:
            if len(desc) >= 2:
                space = " "
                tags = space.join(desc[1:len(desc)]).split(' , ')
                tagged = ", ".join(tags)
                x =  desc[0].split(' | ')
                print(f"{x[0]} ({x[1]}) [{tagged}]")
            else:
                x =  desc[0].split(' | ')
                y = x[1].split(' |')
                print(f"{x[0]} ({y[0]}) []")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        playing = ''
        stopping = ''
        if video_id in self.video:
            for vids in current_play:
                if self.current_play[vids] == 1:
                    stopping = vids
                    self.current_play[vids] -= 1
                    print(f"Stopping video: {stopping}")
                elif self.current_play[vids] == 2:
                    stopping = vids
                    self.current_play[vids] -= 2
                    print(f"Stopping video: {stopping}")
            playing = self.video[video_id]
            self.current_play[playing] += 1
            print(f"Playing video: {playing}")
        else:
            playing = "Video does not exist"
            print(f"Cannot play video: {playing}")

    def stop_video(self):
        """Stops the current video."""
        x = len(self.current_play)
        videos = []
        for video in self.current_play:
            videos.append(video)
        i = 0
        stat = 0
        while i < x:
            if self.current_play[videos[i]] == 1:
                self.current_play[videos[i]] -= 1 
                print(f"Stopping video: {videos[i]}")
                stat = 1
                break
            elif self.current_play[videos[i]] == 2: # if video is paused
                self.current_play[videos[i]] -= 2
                print(f"Stopping video: {videos[i]}")
                stat = 1
                break
            i += 1
        if stat == 0:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        videoIDs = []
        for ids in self.video:
            videoIDs.append(ids)

        video_id = random.choice(videoIDs)
        self.play_video(video_id)

    def pause_video(self):
        """Pauses the current video."""
        x = len(self.current_play)
        videos = []
        for video in self.current_play:
            videos.append(video)
        i = 0
        stat = 0
        while i < x:
            if self.current_play[videos[i]] == 1:
                self.current_play[videos[i]] += 1 
                print(f"Pausing video: {videos[i]}")
                stat = 1
                break
            elif self.current_play[videos[i]] == 2: # if video is already paused
                print(f"Video already paused: {videos[i]}")
                stat = 1
                break
            i += 1
        if stat == 0:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        x = len(self.current_play)
        videos = []
        for video in self.current_play:
            videos.append(video)
        i = 0
        stat = 0
        while i < x:
            if self.current_play[videos[i]] == 1:
                print(f"Cannot contitue video: Video is not paused")
                stat = 1
                break
            elif self.current_play[videos[i]] == 2: 
                print(f"Continuing video: {videos[i]}")
                self.current_play[videos[i]] -= 1
                stat = 1
                break
            i += 1
        if stat == 0:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        x = len(self.required_video)
        videos = []
        cur_video = []
        for video in self.required_video:
            videos.append(video)
        for vid in self.current_play:
            cur_video.append(vid)
        i = 0
        stat = 0
        while i < x:
            if self.current_play[cur_video[i]] == 1:
                tec = self.show_playingVid[videos[i]]
                desc = tec.split(" |  ")
                if len(desc) >= 2:
                    space = ""
                    tags = space.join(desc[0]).split(' | ')
                    tagged = ",".join(desc[1:len(desc)])
                    x =  ", ".join(tagged.split(' , '))
                    print(f"Currently playing: {tags[0]} ({tags[1]}) [{x}]")
                else:
                    space = ""
                    tags = space.join(desc[0]).split(' | ')
                    print(f"Currently playing: {tags[0]} ({tags[0]}) []")
                stat = 1
                break
            elif self.current_play[cur_video[i]] == 2: # if video is paused
                tec = self.show_playingVid[videos[i]]
                desc = tec.split(" |  ")
                if len(desc) >= 2:
                    space = ""
                    tags = space.join(desc[0]).split(' | ')
                    tagged = ",".join(desc[1:len(desc)])
                    x =  ", ".join(tagged.split(' , '))
                    print(f"Currently playing: {tags[0]} ({tags[1]}) [{x}] - PAUSED")
                else:
                    space = ""
                    tags = space.join(desc[0]).split(' | ')
                    print(f"Currently playing: {tags[0]} ({tags[0]}) [] - PAUSED")
                stat = 1
                break
            i += 1
        if stat == 0:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
