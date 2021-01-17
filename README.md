# Rotating-Camera-For-Video-Conferencing-Based-On-Speaker-Voice

## Description

The given "code.py" file was tested for 3 sensors only and the results were satisfactory, this may not work 100% accurately therefore, slight ammendments to the sensitivity of the sensors are needed to be made and tried out, hope it'll workout fine.

## Live VLC Media Player Stream

raspivid -o - -t 0 -n -hf -w 600 -h 400 -fps 12 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264



-o Specifies the output filename. the ‘-‘ beside denotes no filename
-t is the duration of the recoding, 0 being infinity
-hf is Horizontal Flip
-w and -h is the resolution for Width and Height
-fps is Frames per Second
The rest means that on port 8554, data will be sent through http using h264 as stdout using VLC



## INSTRUCTIONS
1. Open VLC Media Player in another device(Mobile or Computer)
2. Go to Media> Open Network Stream> and type http://IPADDRESS:8554//
3. And hit play 
4. Make sure your device is connected to the same WiFi network 
