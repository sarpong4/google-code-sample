"""A video player class."""

from .video_library import VideoLibrary


# Open videos file and parse each line as a list
videos = []
with open('src/videos.txt') as f:
    videos = f.read().splitlines()

# dictionary sets current playing status of all videos to 0 (not playing) - currently playing = 1
current_play = {}

# dictionary that relates vide0_id to video
video = {}
required_video = []
for v in videos:
    v_tagout = v.split(' |  ')
    x = v_tagout[0].split(' | ')
    video[x[1]] = x[0]
    current_play[x[0]] = 0




class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.videos = videos
        self.video = video
        self.current_play = current_play

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
            playing = self.video[video_id]
            self.current_play[playing] += 1
            print(f"Playing video: {playing}")
        else:
            playing = "Video does not exist"
            print(f"Cannot play video: {playing}")

    def stop_video(self):
        """Stops the current video."""

        print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""

        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

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
