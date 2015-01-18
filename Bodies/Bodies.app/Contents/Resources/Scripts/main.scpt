set aPy to get "Bodies.py"
tell application "Finder"
	set aPath to get (path to me as Unicode text)
	set aPath to get (aPath & "Contents:Resources:Python:")
	set aFile to get (aPath & aPy)
	set aBoolean to get exists aFile
	if aBoolean then
		set aDirectory to get POSIX path of aPath
	else
		set aFile to get POSIX path of aFile
		display alert "The python program (" & aFile & ") does not exist."
		return
	end if
end tell
-- set aShellScript to "(cd " & aDirectory & "; python " & aPy & ") ; exit"
-- set aResult to do shell script aShellScript
-- display dialog aResult
tell application "Terminal"
	activate
	do script with command "(cd " & aDirectory & "; python " & aPy & ") ; exit"
	tell front window
		set background color to "black"
		set cursor color to "green"
		set normal text color to "yellow"
		set bold text color to "red"
		set title displays shell path to false
		set title displays window size to false
		set title displays device name to false
		set title displays file name to false
		set title displays custom title to true
		set custom title to "Bodies Transcript"
		set number of columns to 128
		set number of rows to 40
		set position to {25, 50}
	end tell
end tell