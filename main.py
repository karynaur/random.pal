import os
import glob
from transformers import pipeline, Conversation
from gtts import gTTS
from Wav2Lip import inference
import argparse

conversation_pipeline = pipeline('conversational')
"""
  {
    'age': (int)
    'user_id': (int),
    'text': (str)

  }
"""
def main(sentence): 
  if sentence == "favicon.ico":return 
  
  if not os.path.exists(str(sentence['user_id'])):os.mkdir(str(sentence['user_id']))


  tts = gTTS(conversation_pipeline([Conversation(str(sentence['text']))]).generated_responses[0],lang = 'en', tld = 'ca')
  path = './' + str(sentence['user_id'])
  tts.save(path + '/audio.wav')
  age = sentence['age']//20

  args = argparse.Namespace(audio= path + "/audio.wav" , box=[-1, -1, -1, -1], \
  checkpoint_path='Wav2Lip/checkpoints/wav2lip_gan.pth', crop=[0, -1, 0, -1],\
  face=f'./assets/face_{age}.jpg', face_det_batch_size=16, fps=25.0, img_size=96, nosmooth=False,\
  outfile = path + '/result.mp4', pads=[0, 10, 0, 0], resize_factor=1, rotate=False, \
  static=True, wav2lip_batch_size=128)
  
  inference.main(args)
  os.remove(path + '/audio.wav')
  if os.path.exists(path + '/result.mp4'):
      return "SUCESS"
  return "FAIL"
