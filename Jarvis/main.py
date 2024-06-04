from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
import api_key
from langchain.prompts import ChatPromptTemplate
import speech_recognition as sr
import json
import edge_tts
import asyncio
import pygame
import on_off
import pvporcupine
import pyaudio
import struct
import time
import porcupine_key
import sounddevice
import os
def recognize_speech():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something: ")
        audio=recognizer.listen(source)
    try:
        listened=recognizer.recognize_google(audio)
        print("you said: ",listened)
        return listened
    except sr.UnknownValueError:
        print("Sorry,could not understand audio.")
    except sr.RequestError as e:
        print(f"could not request result from Google Speech Recognition service;{e}")
def good_format(lines):
    my_new_lines=lines.replace("JSON","")
    my_new_lines=my_new_lines.replace("json","")
    my_new_lines=my_new_lines[3:-3]
    return my_new_lines
def speak():
    pygame.init()
    pygame.mixer.music.load('test.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    os.remove('test.mp3')
def yesmaster():
    pygame.init()
    pygame.mixer.music.load('yesmaster.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
def jarviscametolive():
    pygame.init()
    pygame.mixer.music.load('jarviscametolive.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
def sorryicouldntunderstand():
    pygame.init()
    pygame.mixer.music.load('sorryicouldntunderstand.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
def beep1():
    pygame.init()
    pygame.mixer.music.load('beep1.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()

def beep2():
    pygame.init()
    pygame.mixer.music.load('beep2.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
def generate_sound(generated):
    VOICE="hi-IN-SwaraNeural"
    OUTPUT_FILE = "test.mp3"
    async def amain() -> None:
        """Main function"""
        communicate = edge_tts.Communicate(generated, VOICE)
        await communicate.save(OUTPUT_FILE)
    asyncio.run(amain())


def ai():
    try:
        beep1()
        question=recognize_speech()

        chat_llm=ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=api_key.GOOGLE_API_KEY)
        template_string = """
        You are an AI Assistant named Jarvis, specializing in smart home control. Your output is strictly in JSON format.

User Preferences:
* Going to office: Switch off all Parent Bedroom devices
* Going to school: Switch off all Child Bedroom devices
* Coming back from office: Switch on Living Room AC
* "I am feeling cold": Switch off AC 
* "I am going to bath": Switch on Geyser, Washroom Bulb
* "Taken bath": Switch off Geyser, Washroom Bulb
* Going to market: Switch off all equipment of Parent Bedroom
* Going to sleep: Switch off all lighting equipment that is bulb

Equipment List:
* Parent Bedroom: Parent Bedroom Bulb, Parent Bedroom Fan, Parent Bedroom AC
* Child Bedroom:  Child Bedroom Bulb, Child Bedroom Fan, Child Bedroom AC, Child Study Lamp
* Living Room: Living Room Bulb, Living Room AC, Living Room Fan
* Washroom: Geyser,Washroom Bulb
* Kithcen: Kitchen Bulb
* For filling Water: Motor Pump

        query: ```{query}```

        Format the output as JSON with the following keys:
        switched_on_equipments
        reply_I_have_switched_on_this_this_and_this
        switched_off_equipments
        reply_I_have_switched_off_this_this_and_this
        """
        prompt_template=ChatPromptTemplate.from_template(template_string)
        output1=prompt_template.messages[0].prompt
        print(output1)
        branding_messages = prompt_template.format_messages( query=f"{question}")
        print(branding_messages)
        consultant_response=chat_llm(branding_messages)
        print(consultant_response.content)
        output3=consultant_response.content
        print(type(output3))
        f=open('instruction.json','w')
        f.write(good_format(consultant_response.content))
        f.close()
        with open('instruction.json') as f:
            data=json.load(f)

            
        for device_on in data['switched_on_equipments']:
            if(device_on.lower()=='Parent Bedroom Bulb'.lower()):
                on_off.p_bedroom_bulb_on()
            if(device_on.lower()=='Parent Bedroom Fan'.lower()):
                on_off.p_fan_on()
            if (device_on.lower()=='Parent Bedroom AC'.lower()):
                on_off.p_AC_on()
            if(device_on.lower()=='Child Bedroom Bulb'.lower()):
                on_off.c_bedroom_bulb_on()
            if(device_on.lower()=='Child Bedroom Fan'.lower()):
                on_off.c_fan_on()
            if(device_on.lower()=='Child Bedroom AC'.lower()):
                on_off.c_AC_on()
            if(device_on.lower()=='Child Study Lamp'.lower()):
                on_off.c_study_lamp_on()
            if(device_on.lower()=='Kitchen Bulb'.lower()):
                on_off.k_bulb_on()
            if(device_on.lower()=='Washroom Bulb'.lower()):
                on_off.w_bulb_on()
            if(device_on.lower()=='Living Room Bulb'.lower()):
                on_off.l_bulb_on()
            if(device_on.lower()=='Living Room Fan'.lower()):
                on_off.l_fan_on()
            if(device_on.lower()=='Living Room AC'.lower()):
                on_off.l_AC_on()
            if(device_on.lower()=='Motor Pump'.lower()):
                on_off.motor_on()
        for device_off in data['switched_off_equipments']:
            if(device_off.lower()=='Parent Bedroom Bulb'.lower()):
                on_off.p_bedroom_bulb_off()
            if(device_off.lower()=='Parent Bedroom Fan'.lower()):
                on_off.p_fan_off()
            if (device_off.lower()=='Parent Bedroom AC'.lower()):
                on_off.p_AC_on()
            if(device_off.lower()=='Child Bedroom Bulb'.lower()):
                on_off.c_bedroom_bulb_off()
            if(device_off.lower()=='Child Bedroom Fan'.lower()):
                on_off.c_fan_off()
            if(device_off.lower()=='Child Bedroom AC'.lower()):
                on_off.c_AC_off()
            if(device_off.lower()=='Child Study Lamp'.lower()):
                on_off.c_study_lamp_off()
            if(device_off.lower()=='Kitchen Bulb'.lower()):
                on_off.k_bulb_off()
            if(device_off.lower()=='Washroom Bulb'.lower()):
                on_off.w_bulb_off()
            if(device_off.lower()=='Living Room Bulb'.lower()):
                on_off.l_bulb_off()
            if(device_off.lower()=='Living Room Fan'.lower()):
                on_off.l_fan_off()
            if(device_off.lower()=='Living Room AC'.lower()):
                on_off.l_AC_off()
            if(device_off.lower()=='Motor Pump'.lower()):
                on_off.motor_off()
        if data['reply_I_have_switched_on_this_this_and_this']!=None:
            if data['reply_I_have_switched_on_this_this_and_this']!="":
                generate_sound(data['reply_I_have_switched_on_this_this_and_this'])
                speak()
        if data['reply_I_have_switched_off_this_this_and_this']!=None:

            if data['reply_I_have_switched_off_this_this_and_this']!="":
                generate_sound(data['reply_I_have_switched_off_this_this_and_this'])
                speak()
        beep2()
    except sr.UnknownValueError:
        sorryicouldntunderstand()
    except sr.RequestError as e:
        sorryicouldntunderstand()
    except Exception as e:
        sorryicouldntunderstand()
        print(f"Error encountered: {e}")
def main():
    time.sleep(10)
    jarviscametolive()
    porcupine=None
    pa=None
    audio_stream=None

    print("J.A.R.V.I.S. version 1.2- Online and Ready! ")
    print("************************************************")
    print("J.A.R.V.I.S.: Awaiting your call")

    try:
        porcupine=pvporcupine.create(keywords=["jarvis","computer"],
        access_key=porcupine_key.access_key                             
        )
        pa=pyaudio.PyAudio()
        audio_stream=pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length)
        
        while True:
            pcm=audio_stream.read(porcupine.frame_length)
            pcm=struct.unpack_from("h"*porcupine.frame_length,pcm)

            keyword_index=porcupine.process(pcm)
            if keyword_index>=0:
                yesmaster()
                time.sleep(1)
                ai()
                print("J.A.R.V.I.S.: Awaiting your call Sir")
    finally:
        if porcupine is not None:
            porcupine.delete()


main()
    
            
    
        
