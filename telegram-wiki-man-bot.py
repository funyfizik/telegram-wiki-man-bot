import telebot, emoji, wikipedia, re, os, time, subprocess

bot = telebot.TeleBot('<bot_id>');
#select lang in Wikipedia
wikipedia.set_lang("ru")
#pip install wikipedia

def run_forever(): #def bot crash
    try:
        #clear wiki trash symsols
        def getwiki(s):
            try:
                ny = wikipedia.page(s)
        # Get 4k symbols from wiki
                wikitext=ny.content[:4000]
        # delimiter dot
                wikimas=wikitext.split('.')
                wikimas = wikimas[:-1]
                wikitext2 = ''
                for x in wikimas:
                    if not('==' in x):
                        if(len((x.strip()))>3):
                            wikitext2=wikitext2+x+'.'
                    else:
                        break
        #delete special symbols
                wikitext2=re.sub('\([^()]*\)', '', wikitext2)
                wikitext2=re.sub('\([^()]*\)', '', wikitext2)
                wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
                return wikitext2
            except Exception as e:
                return 'There no info about it'
        @bot.message_handler(content_types=["text"])
        def handle_text(message):
            if "help" in message.text.lower():
                bot.send_message(message.chat.id, "Привет, Я бот и я умею показывать странички вики командой W(ограничение 4к символов), а также я умею показывать мануалы линукс командой M!(ограничение 32768 символов)")
            if "w " in message.text[:2] or "W " in message.text[:2]:
                message.text = message.text[2:]
                bot.send_message(message.chat.id, getwiki(message.text))
            if "m " in message.text[:2].lower():
                cmd = 'man' + ' ' + message.text[2:]
                print(cmd)
                bash =  os.popen(cmd).read()
                print(bash)
                bot.send_message(message.chat.id, bash[:4095]) #make messages by 4k symnbols TG limit
                    bot.send_message(message.chat.id, bash[4096:8192])
                    if len(bash) > 8192:
                        bot.send_message(message.chat.id, bash[8192:12288])
                        if len(bash) > 12288:
                            bot.send_message(message.chat.id, bash[12288:16384])
                            if len(bash) > 16384:
                                bot.send_message(message.chat.id, bash[16384:20480])      
                                if len(bash) > 20480:
                                    bot.send_message(message.chat.id, bash[20480:24576])  
                                    if len(bash) > 24576:
                                        bot.send_message(message.chat.id, bash[24576:28672])
                                        if len(bash) > 28672:
                                            bot.send_message(message.chat.id, bash[28672:32768])                                        
        bot.polling(none_stop=True, interval=0)
        raise Exception("Error simulated!")
        except Exception:
        print("Something crashed your program. Let's restart it")
        run_forever() # Careful.. recursive behavior
        # Recommended to do this instead
        handle_exception()

def handle_exception():
    # code here
    pass

run_forever()
