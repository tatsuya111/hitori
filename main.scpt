set aPy to get "Bodies.py" 
tell application "Finder"
			set aFile to get (aPath & aPy)
			tell front window
				set cursor color to "green"
				set bold text color to "red"
				set title displays window size to false 
				set title displays device name to false set title displays file name to false 
				set title displays custom title to true set custom title to "Bodies Transcript" 
				set number of columns to 128
			end tell