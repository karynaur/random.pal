# random.pal
Your AI assistant is always here to listen and talk. 

## Inspiration
Bored? Need to talk to someone? Here's an AI companion that is always here to listen and talk. Our product is a mobile app that lets you talk to a random person, that does not exist. 

## What it does
Modern technology like the google assistant and Apple Siri are only capable of responding to text messages. We built a mobile app powered by Deep Learning conversational models and "deep fake" technology with which you can video call an AI assistant and not worry about your data getting leaked _coughs_

## How we built it
1. User open the app on phone and starts a video call after choosing the age of the assistant.
2. A random AI assistant gets assigned, images of people are scraped from [thispersondoesnotexist.com](https://thispersondoesnotexist.com) 
3. The user then taps the mike to talk to the assistant, which gets converted to text by inbuilt google **speech-to-text**.
4. The text along with the age chosen and a unique user_id will be sent to the firebase database.
5. Flask server actively running on a Google Cloud Virtual Machine will keep listening for changes in the database.
6. The json object is retrieved from the database calls the python script which has 4 functions<br>
       1. Scrape the image of a person-who-does-not-exist depending on the age selected by the user<br>
       2. Run the text through a conversational model that uses State of the Art deep learning <br>architecture Transformers to get responses the user input<br>
       3. Google text to speech model that converts model outputs to speech<br>
       4. The audio file along with the photo of the previously selected image sent to a Wav2lip Model.<br> Wav2Lip is a State of the Art deep learning model for Lip Sync, which takes an image and an audio file and returns a video of the person lip-syncing to the audio.<br>
7. The video is sent back to the app that displays it on the screen.

## Challenges we ran into
Understanding how the models work and integrating flask, GCP and firebase

## Accomplishments that we're proud of
A working end to end model, that takes in user voice to give out a video of a person conversing with the user, all in one app.

## What we learned
We learned how to integrate huggingface transformers into an application. We had the opportunity to learn how android studio works and make an end-to-end android application. We also got introduced to GCP and how to run/stop/SSH into instances.

## What's next for random.pal
Host the model on a GPU instance in GCP which will reduce the lag by a huge margin. Removing the mic button completely, and implement Realtime voice recognition and then responses based on that
