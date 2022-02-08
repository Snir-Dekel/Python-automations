# Using Deep Learning to Mute my microphone when I get up from my chair!
## when you are in a voice chat (zoom, discord, etc.) and going for a minute, you need to mute your mic, this project solves this problem by automatically muting the mic when when you get up from your chair.
# How I made it:
> ## Go to https://teachablemachine.withgoogle.com/train and choose"Audio Project"

> ![image](https://user-images.githubusercontent.com/66528853/152966660-40941362-0365-42de-85e7-a91e5f43c495.png)
> ## Record Your Background Noise (You speaking, Silent, etc.) and the sound your chair makes when you get up (record as much samples as you can)

> ![image](https://user-images.githubusercontent.com/66528853/152967241-a36d3c67-21be-4874-b1f3-234f71db9e13.png)

> ## Then press Train Model and export it (You can even try the classification on the website)

![image](https://user-images.githubusercontent.com/66528853/152967735-6e163379-c5ab-45b9-b7ef-f5aa2f0cdb47.png)

> ## Upload the model

![image](https://user-images.githubusercontent.com/66528853/152968005-b40fef94-4d6a-4f9a-9958-f74c777593df.png)

> ## Open the web editor

![image](https://user-images.githubusercontent.com/66528853/152968200-32375ee8-22f3-42cc-ad07-e50fb1479208.png)

> ## Copy the code from `sketch.js` in this repository and paste it instead the `sketch.js` in the web editor **replace the soundModelURL to the url of model you created**

![image](https://user-images.githubusercontent.com/66528853/152969162-68f2c037-fc72-4985-bdc9-7a85d839275e.png)
![image](https://user-images.githubusercontent.com/66528853/152969160-459f6b9b-a4e3-49f0-b56f-a84ef95c5318.png)

> ## **Last step!** download `code.py` from this repository (install the requirements by running pip install -r requirements.txt)

> ## After running the code, a browser contoller by python will be opened, and you will see this screen, which means the model detecting background noise

![image](https://user-images.githubusercontent.com/66528853/152970782-2599c11f-59f4-43e1-b5c6-31eb119f8a28.png)

> ## When chair is detected by the model, this screen will show up python will detect it and mute your mic automatically!

![image](https://user-images.githubusercontent.com/66528853/152970997-f23579de-8a80-4288-be58-599b3a080c46.png)

