This python3 script is for exporting tracklists directly from an Ableton session file. Raison d'etre is that I thought there must be a way to do this that doesn't involve writing it down myself!

- Upon executing, a file select window lets you select a .als file. 
- The names and start times of all audioclips in the arrangement view (not the session / clip view) are extracted. The names assigned to the clips in Ableton are used, not the names of the files on disk.
- The start times are converted into MM:SS format timestamps.
	- 120 bpm is assumed throughout the project! Compensation for tempo variation might be added at a later time.
- Also some attempts are made to remove anything from the clip names that is not Artist - Title.

If all goes well, your output should read something like:

`Found 27 tracks in coolmix.als.`

`Created tracklist at /fullpath/coolmix tracklist.txt`
