import re
from telegram.error import BadRequest
import datetime
import json
import asyncio
from telegram.error import TimedOut
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, CommandHandler, CallbackContext, filters

TOKEN = 'YOUR TOKEN'
CHANNEL_ID = 'YOU CHANNEL' # Replace with your channel's username or ID
POST_IDS_FILE = 'post_ids.json'

async def save_post_ids(post_ids, last_updated_index=0):
    with open(POST_IDS_FILE, 'w') as f:
        json.dump({'post_ids': post_ids, 'last_updated_index': last_updated_index}, f)

async def load_post_data():
    try:
        with open(POST_IDS_FILE) as f:
            data = json.load(f)
            return data['post_ids'], data.get('last_updated_index', 0)
    except FileNotFoundError:
        return None, 0

async def create_main_post(update: Update, context: CallbackContext) -> None:
    post_ids, _ = await load_post_data()
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")

    keyboard = [
        [InlineKeyboardButton("💎 Купить 💎", url="https://t.me/CHANNEL")],
        [InlineKeyboardButton("📱 iPhone 16", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[12]}")],
        [InlineKeyboardButton("📱 iPhone 15", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[11]}"),
         InlineKeyboardButton("📱 iPhone 14", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[10]}")],
        [InlineKeyboardButton("📱 iPhone 13", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[9]}"),
         InlineKeyboardButton("📱 SE 11 12", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[8]}")],
        [InlineKeyboardButton("📺 iPad", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[2]}"),
         InlineKeyboardButton("⌚ Apple Watch", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[0]}")],
        [InlineKeyboardButton("💻 Macbook 💻", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[5]}")],
         [InlineKeyboardButton("🎧 AirPods / Dyson / 🎮 PS 5 ", url=f"https://t.me/CHANNEL/101")],
        [InlineKeyboardButton("⚡️ Б/У устройства ⚡️", url=f"https://t.me/CHANNEL/98")],
        [InlineKeyboardButton("🌐 Гарантия / Ремонт ⚙️", url=f"https://t.me/CHANNEL/93")],
    
   [InlineKeyboardButton("👌 Отзывы 👌", url=f"https://t.me/@CHANNEL")] ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    photo_file = open('path_to_your_image.jpg', 'rb')  # Replace 'path_to_your_image.jpg' with the actual path to your image file
    caption_text = f"Актуальные цены от \n{current_date}\n\nВсё строго оригинал! В наличии.\nПо заказам: @romansergeevich14"
    photo_message = await context.bot.send_photo(chat_id=CHANNEL_ID, photo=photo_file, caption=caption_text, reply_markup=reply_markup)
  
    post_ids.append(photo_message.message_id)
    await update.message.reply_text('главный пост создан.')



async def create_initial_posts(update: Update, context: CallbackContext) -> None:
    post_ids, _ = await load_post_data()
    if post_ids is not None:
        await update.message.reply_text('Посты уже были созданы.')
        return

    post_ids = []
    
    for _ in range(14):  # Increase the number to 8 as per your need
        try:
            message = await context.bot.send_message(chat_id=CHANNEL_ID, text="Placeholder for text processing")
            post_ids.append(message.message_id)
            await asyncio.sleep(10)  # Sleep for 1 second between messages
        except TimedOut:
            await update.message.reply_text("Ошибка: Превышено время ожидания сообщения.")
            continue

    current_date = datetime.datetime.now().strftime("%d.%m.%Y")

    keyboard = [
        [InlineKeyboardButton("💎 Купить 💎", url="https://t.me/CHANNEL")],
        [InlineKeyboardButton("📱 iPhone 16", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[12]}")],
        [InlineKeyboardButton("📱 iPhone 15", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[11]}"),
         InlineKeyboardButton("📱 iPhone 14", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[10]}")],
        [InlineKeyboardButton("📱 iPhone 13", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[9]}"),
         InlineKeyboardButton("📱 SE 11 12", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[8]}")],
        [InlineKeyboardButton("📺 iPad", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[2]}"),
         InlineKeyboardButton("⌚ Apple Watch", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[0]}")],
        [InlineKeyboardButton("💻 Macbook 💻", url=f"https://t.me/{CHANNEL_ID[1:]}/{post_ids[5]}")],
         [InlineKeyboardButton("🎧 AirPods / Dyson / 🎮 PS 5 ", url=f"https://t.me/CHANNEL/101")],
        [InlineKeyboardButton("⚡️ Б/У устройства ⚡️", url=f"https://t.me/CHANNEL/98")],
        [InlineKeyboardButton("🌐 Гарантия / Ремонт ⚙️", url=f"https://t.me/CHANNEL/93")],
    
   [InlineKeyboardButton("👌 Отзывы 👌", url=f"https://t.me/@CHANNEL")] ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    photo_file = open('path_to_your_image.jpg', 'rb')  # Replace 'path_to_your_image.jpg' with the actual path to your image file
    caption_text = f"Актуальные цены от \n{current_date}\n\nВсё строго оригинал! В наличии.\nПо заказам: @romansergeevich14"
    photo_message = await context.bot.send_photo(chat_id=CHANNEL_ID, photo=photo_file, caption=caption_text, reply_markup=reply_markup)
  
    post_ids.append(photo_message.message_id)

    await save_post_ids(post_ids)
    await update.message.reply_text('Начальные посты созданы.')

async def set_loading_text(context: CallbackContext, chat_id, message_id):

    try:
        await context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="загрузка")
        await asyncio.sleep(10)  # Add delay after updating a post
    except BadRequest as e:
        print(f"Ошибка при установке текста 'загрузка': {e.message}")

async def process_and_reply(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")

    def center_text_with_symbol(text, symbol, width=30, add_break_after=False):
        total_padding = width - len(text)
        left_padding = total_padding // 2
        right_padding = total_padding - left_padding
        centered_text = f"{' ' * left_padding}{symbol}{text}{symbol}{' ' * right_padding}"
        if add_break_after:
            centered_text += '\n'
        return centered_text
    

    updated_text_lines = [
        center_text_with_symbol("Актуальный прайс-лист", '', 30),

        "",
        center_text_with_symbol("Новые ", '🆕', 30),
        ""
    ]

    def escape_markdown(text: str) -> str:
        escape_chars = r"_*[]()~`>#+-=|{}.!"
        for char in escape_chars:
            text = text.replace(char, f"\\{char}")
        return text

    last_model = ""
    last_memory_size = ""
    data = escape_markdown(str(current_date))
    link = center_text_with_symbol("[" + data + "](https://t.me/CHANNEL)", '', 30)

    if 'ipad' in text.lower():
        
        data = escape_markdown(str(current_date))

        if 'ipad air' in text.lower():
            link = center_text_with_symbol("[" + data + "](https://telegra.ph/file/5d833cb7908a20caa5ba4.jpg)", '', 30)
        elif 'ipad pro' in text.lower():
            link = center_text_with_symbol("[" + data + "](https://telegra.ph/file/a4465747f74f6760dd887.jpg)", '', 30)
        else:
            link = center_text_with_symbol("[" + data + "](https://t.me/romansergeevich142)", '', 30)


        memnow = ''
        now_model = ''
        for line in text.split('\n'):
            probel = ''
            if any(unwanted in line.lower() for unwanted in ['nano','обменка', 'актив', 'уценка', 'демо', 'заменен', 'не актив', 'коцка', '🇨🇳', '🚘', 'magic']):
                continue
            if any(unwanted in line.lower() for unwanted in ['ipad','mini','air']):
                if ('ipad' in line.lower()):
                    True
                else:
                    line = 'iPad ' + line

                if ('rfb' in line.lower()):
                    True
                else:
                    try:
                        Ipad = re.compile(r'(?:(ipad|mini|air|pad))(?:\s(mini \d+| air \d+|air \d+|pro 11|pro 12.9|pro 12|pro 13|\d+))?', re.IGNORECASE)
                        ipad = Ipad.search(line).group()
                    except:
                        continue
                    Core = re.compile('(m1|m2|m4|m3)', re.IGNORECASE)
                    Memory = re.compile(r'(64 |256 |128 |\d+TB |512 |\d+GB |\d+ TB )', re.IGNORECASE)
                    Color = re.compile('(silver|Gray|Grey|White|Purple|Starlight|Pink|Yellow|Blue|Space Black|Black|Space Black|starlig|Space)', re.IGNORECASE)
                    WL = re.compile('(WIFI|LTE|Wi-fi|wi- fi|wi|sim|5g)', re.IGNORECASE)
                    Price = re.compile(r'-\d+.\d+|- \d+.\d+|\b\d+\.\d+\b', re.IGNORECASE)
                    try:
                        core = ''
                        memory = Memory.search(line).group()

                        if memnow == memory:
                            True
                        else:
                            memnow = memory
                            probel = '\n'

                        color = Color.search(line).group()
                        wl = WL.search(line).group()
                        try:
                            sub_line = line
                            try:
                                line = line.split('12.9')[1]
                            except:
                                True
                            try:
                                line = line.split('10.2')[1]
                            except:
                                True
                            #price = Price.search(line).group()[1:]
                            price = re.search(r'\b\d+\.\d+\b', line.lower()).group()
                        except:
                            continue
                        line = sub_line
                        price = str(int(price.split('.')[0]) + 5) + '.' + price.split('.')[1]

                        try:
                            core = Core.search(line).group()
                        except:
                            True

                        full_model_name = probel + ipad + ' ' + memory + color + ' ' + core + ' ' + wl + ' - ' + price + ' ₽'
                        updated_text_lines.append(full_model_name)
                        probel = ''
                    except:
                        core = ''
                        try:
                            core = Core.search(line).group()
                        except:
                            True
                            full_model_name = ipad + ' ' + core
                            if full_model_name.lower() == now_model.lower():
                                continue
                            now_model = ipad + ' ' + core
                        centered_model_name = center_text_with_symbol(ipad + ' ' + core, '🔥', 30, add_break_after=True)
                        updated_text_lines.append('\n' + centered_model_name)

    elif 'macbook' in text.lower():
        last_size = ''
        last_mac = ''
        memnow = ''
        now_model = ''

        data = escape_markdown(str(current_date))
        if 'air' in text.lower():
            link = center_text_with_symbol("[" + data + "](https://telegra.ph/file/0a341086179ba05e4868a.jpg)", '', 30)
        else:
            link = center_text_with_symbol("[" + data + "](https://telegra.ph/file/e5b7c8c5bfcc4faf68423.jpg)", '', 30)
        

        for line in text.split('\n'):
            if ('🚚' in line.lower()):
                continue
            if ('🚘' in line.lower()):
                continue
            probel = ''
            if any(unwanted in line.lower() for unwanted in ['обменка', 'актив', 'уценка', 'демо', 'заменен', 'не актив', 'коцка']):
                continue
            if any(unwanted in line.lower() for unwanted in ['macbook','air','pro','max','m1','m2','m3','m4']):
                if ('macbook' in line.lower()):
                    True
                else:
                    line = 'MacBook ' + line
                

                if ('rfb' in line.lower()):
                    continue
                if ('mini' in line.lower()):
                    continue
                else:
                    try:
                        MacBook = re.compile(r'(pro|air)', re.IGNORECASE)
                        macbook = MacBook.search(line).group()
                        last_mac = macbook
                    except:
                        macbook = last_mac
                    Size = re.compile('13 |15 |14 |16 |\d+"')
                    Memory = re.compile(r'(512|\d+/\d+TB|\d+/\d+ TB|\d+/\d+ |,\d+/\d+|\d+/\d+|\d+ТБ|\d+tb|\d+ ТБ|\d+ гб|\d+ tb|\d+GB, \d+GB|\d+GB, \d+ GB|\d+GB, \d+TB|\d+GB/\d+GB)', re.IGNORECASE)
                    Color = re.compile('(space black|gray|gold|silver|midnight|starlight|space gray|spacegray|grey|black|sky blue)', re.IGNORECASE)
                    Price = re.compile('-\d+.\d+|- \d+.\d+|- \d+,\d+', re.IGNORECASE)
                    try:
                        memory = Memory.search(line).group()
                        print(memory)

                        if memnow == memory:
                            True
                        else:
                            memnow = memory
                            probel = '\n'
                        
                        if 'tb' in line.lower():
                            if 'tb' in memory.lower():
                                True
                            else:
                                memory += 'TB' 
                       
                        try:
                            color = Color.search(line).group()
                        except:
                            continue
                        
                        try:
                            price = Price.search(line).group()[1:]
                        except:
                            continue
                        price = str(int(price.split('.')[0]) + 5) + '.' + price.split('.')[1]

                        Core = re.compile('m\d+ max|m\d+ pro|m\d+|m2', re.IGNORECASE)
                        core = Core.search(line).group()

                        try:
                            size = Size.search(line).group()
                            last_size = size
                        except:
                            size = last_size

                        full_model_name = probel + 'Macbook '+ macbook + ' ' + size + core + ' ' + memory + ' ' + color + ' - ' + price + ' ₽'
                        updated_text_lines.append(full_model_name)
                        probel = ''
                    except:
                        try:
                            size = Size.search(line).group()
                            full_model_name = 'Macbook ' + macbook + ' ' +size
                            if full_model_name.lower() == now_model.lower():
                                continue
                            now_model = 'Macbook ' + macbook + ' ' +size
                            centered_model_name = center_text_with_symbol('Macbook ' + macbook + ' ' +size, '🔥', 30, add_break_after=True)
                            updated_text_lines.append('\n' + centered_model_name)
                        except:
                            full_model_name = 'Macbook ' + macbook 
                            if full_model_name.lower() == now_model.lower():
                                continue
                            now_model = 'Macbook ' + macbook 
                            centered_model_name = center_text_with_symbol('Macbook ' + macbook, '🔥', 30, add_break_after=True)
                            updated_text_lines.append('\n' + centered_model_name)
                

    elif 'watch' in text.lower():
        vipmodel = ''
        vip = ''
        asize = ''
        probel = ''
        now_model = ''

        data = escape_markdown(str(current_date))
        link = center_text_with_symbol("[" + data + "](https://telegra.ph/file/a8af678ea34649ddc02c8.jpg)", '', 30)

        for line in text.split('\n'):
            if ('🚗' in line.lower()):
                continue
            if ('🚚' in line.lower()):
                continue
            if ('🚘' in line.lower()):
                continue
            if any(unwanted in line.lower() for unwanted in ['watch','s8','s9','s10','ultra']):
                if ('watch' in line.lower()):
                    True
                else:
                    if 'ultra' in line.lower():
                        True
                    else:
                        line = 'watch ' + line
                
                
                try:
                    Model = re.compile(r'(?:(SE 2023 |SE 2 |SE |2 \d+ Ultra |S8 |8 |S9 |S10 |9 |Ultra 2 |Ultra|series 9))', re.IGNORECASE)
                    model = Model.search(line).group()
                except:
                    continue

                if (model == vipmodel):
                    continue
                else:
                    True

                if ('vip' in line.lower()):
                    vip = 'vip'
                    continue
                if (vip == 'vip'):
                    vipmodel = model
                    vip = ''
                    continue

                Size = re.compile(r'(?:(40|44|41|45|49|46|42))', re.IGNORECASE)

                Color = re.compile(r'(?:Titanium (?:(Blue Alpine Loop|Green|Gray))|Black Milanese|Black Ocean Band|Natural Milanese|Natural|Blue Alpine Loop|silver blue|jet black|rose gold|Olive Alpine Loop|green Alpine loop|orange alpine loop|Indigo Alpine Loop|alpine orange|(Ocean Band (?:(Blue|white|Orange)))|(Steel Sport (?:(Gold Clay|Graphite Midnight)))|(Milanese (?:(gold|natural|slate|black|silver))|White-Blue|White/Blue|Black|Midnight|Starlight|Blue|Silver|Red|Pink|Gold|Graphite|white))', re.IGNORECASE)
                Remsize = re.compile(r'(?:(Sport Loop|M/L|S/M|SM|ML|M/L))', re.IGNORECASE)
                Remsizeplus = re.compile(r'(?:(?:(Blue Flame Nike|Cargo Khaki Nike|Desert stone Nike|Midnight|Mulberry|Purе Platinum Nike|Winter Blue)) Sport Band)', re.IGNORECASE)
                Price = re.compile('-\d+.\d+|- \d+.\d+', re.IGNORECASE)

                try:
                    size = Size.search(line).group()
                    if asize == size:
                        probel = ''
                        True
                    else:
                        probel = '\n'
                        asize = size
                    color = Color.search(line).group()
                    price = Price.search(line).group()[1:]
                    price = str(int(price.split('.')[0]) + 5) + '.' + price.split('.')[1]
                    try:
                        remsize = Remsize.search(line).group()
                        try:
                            remsizeplus = Remsizeplus.search(line).group()
                            full_model_name = probel + 'Apple Watch ' + model + ' ' + size + ' ' + color + ' ' + remsizeplus + ' ' + remsize + ' - ' + price + ' ₽'
                            updated_text_lines.append(full_model_name)
                        except:
                            full_model_name = probel + 'Apple Watch ' + model + ' ' + size + ' ' + color + ' ' + remsize + ' - ' + price + ' ₽'
                            updated_text_lines.append(full_model_name)
                    except:
                        full_model_name = probel + 'Apple Watch ' + model + ' ' + size + ' ' + color + ' - ' + price + ' ₽'
                        updated_text_lines.append(full_model_name)
                except:
                    if 'vip' in line.lower():
                        full_model_name = 'Apple Watch ' + model + ' VIP'
                        centered_model_name = center_text_with_symbol(full_model_name, '🔥', 30, add_break_after=True)
                        updated_text_lines.append('\n' + centered_model_name)
                    else:
                        full_model_name = 'Apple Watch ' + model
                        if full_model_name.lower() == now_model.lower():
                            continue
                        now_model = 'Apple Watch ' + model
                        centered_model_name = center_text_with_symbol(full_model_name, '🔥', 30, add_break_after=True)
                        updated_text_lines.append('\n' + centered_model_name)

    else:
        memnow = ''
        colnow = ''
        now_model = ''

        data = escape_markdown(str(current_date))
        if 'iphone 12' in text.lower():
            link = center_text_with_symbol("[" + data + "](https://telegra.ph/file/c8d49e6c1718750022d04.jpg)", '', 30)
        elif 'iphone 13' in text.lower():
            link = center_text_with_symbol("[" + data + "](https://telegra.ph/file/e7c511bdf61f34beb2637.jpg)", '', 30)
        elif '14 pro' in text.lower():
            link = center_text_with_symbol("[" + data + "](https://telegra.ph/file/7921d3a0784378548ad19.jpg)", '', 30)
        elif '15 pro' in text.lower():
            link = center_text_with_symbol("[" + data + "](https://telegra.ph/file/8eee08d896adf401cd6ec.jpg)", '', 30)
        elif '16e' in text.lower():
            link = center_text_with_symbol("[" + data + "](https://telegra.ph/file/7cbe496e7c7fa8bd4054d.jpg)", '', 30)
        else:
            link = center_text_with_symbol("[" + data + "](https://telegra.ph/file/1bdb36319569f6d88503a.jpg)", '', 30)

        for line in text.split('\n'):
            probel = ''
            if any(unwanted in line.lower() for unwanted in ['упаковка','обменка', 'актив', 'уценка', 'демо', 'заменен', 'не актив', 'коцка', '🇨🇳', '🇨🇳', '🇭🇰', '🚗','🚘','сц']):
                continue
            try:
                Memory = re.compile('(64|256|128|\d+TB|512|\d+GB)', re.IGNORECASE)
                memory = Memory.search(line).group()
            except:
                continue
            if ('📱' in line.lower()):
                    True
            else:
                line = '📱 ' + line

            if ('rfb' in line.lower()):
                True
            else:
                try:
                    iPhone = re.compile('(16E |16Е |14 |15 |16 |11 |12 |13 |SE2 |SE 3|SE3 )', re.IGNORECASE)
                    iphone = iPhone.search(line).group()
                except:
                    continue
                if ('15' in line.lower() and '🇺🇸' in line.lower()): 
                    continue
                elif ('14' in line.lower() and '🇺🇸' in line.lower()):
                    continue
                elif ('16' in line.lower() and '🇺🇸' in line.lower()):
                    continue
                else:
                    Model = re.compile('(Plus|Pro Max|Pro|mini)', re.IGNORECASE)
                    Memory = re.compile('(64 |256 |128 |\d+TB |512 |\d+GB )', re.IGNORECASE)
                    Color = re.compile('(Teal|Ultramarine|Desert|blue|Midnight|Starlight|Purple|Yellow|Red|Gold|Silver|black|green|Pink|white|natural|graphite|whte)', re.IGNORECASE)
                    Price = re.compile('-\d+.\d+|- \d+.\d+', re.IGNORECASE)
                    try:
                        memory = Memory.search(line).group()
                        color = Color.search(line).group()

                        if memnow == memory:
                            True
                            if color == colnow:
                                continue
                            else:
                                colnow = color
                        else:
                            colnow = ''
                            memnow = memory
                            probel = '\n'


                        try:
                            model = Model.search(line).group()
                        except:
                            model = ''

                        
                        price = Price.search(line).group()[1:]
                        price = str(int(price.split('.')[0]) + 5) + '.' + price.split('.')[1]

                        full_model_name = probel + iphone + ' ' + model + ' ' + memory + color + ' - ' + price + ' ₽'
                        updated_text_lines.append(full_model_name)
                        probel = ''
                    except:
                        try: 
                            model = Model.search(line).group()
                            if 'pro max' in line.lower():
                                model = 'Pro Max' 
                            fulname = 'iPhone ' + iphone + model
                            if fulname == now_model:
                                continue
                            now_model = 'iPhone ' + iphone + model
                            centered_model_name = center_text_with_symbol(fulname, '🔥', 30, add_break_after=True)
                            updated_text_lines.append('\n' + centered_model_name)
                        except:
                            fulname = 'iPhone ' + iphone
                            if fulname.lower() == now_model.lower():
                                continue
                            now_model = 'iPhone ' + iphone
                            centered_model_name = center_text_with_symbol('iPhone ' + iphone, '🔥', 30, add_break_after=True)
                            updated_text_lines.append('\n' + centered_model_name)
            
    updated_text_lines.extend([
        "",
        center_text_with_symbol("@CHANNEL", '🕴', 30, add_break_after=True),
        center_text_with_symbol("Вся техника новая, не актив, в наличии !", '', 30), 
        center_text_with_symbol("Обновляется каждый день", '⏰', 30) 
    ])
    updated_text = '\n'.join(updated_text_lines)

    def escape_markdown(text: str) -> str:
        escape_chars = r"_*[]()~`>#+-=|{}.!"
        for char in escape_chars:
            text = text.replace(char, f"\\{char}")
        return text

    updated_text = escape_markdown(updated_text)

    updated_text = link + "\n\n" + updated_text

    post_ids, last_updated_index = await load_post_data()
    if not post_ids:
        await update.message.reply_text('Посты не были созданы.')
        return

    target_post_id = post_ids[last_updated_index]
    await set_loading_text(context, CHANNEL_ID, target_post_id)
    try:
        await context.bot.edit_message_text(chat_id=CHANNEL_ID, message_id=target_post_id, text=updated_text, parse_mode="MarkdownV2")
        await asyncio.sleep(10)  # Add delay after updating a post
    except BadRequest as e:
        if "Message is not modified" in e.message:
            updated_text += "\u200B"  # ZERO WIDTH SPACE
            try:
                await context.bot.edit_message_text(chat_id=CHANNEL_ID, message_id=target_post_id, text=updated_text)
            except BadRequest as e:
                print(f"Ошибка при повторной попытке обновления сообщения: {e.message}")
        else:
            print(f"Ошибка при обновлении сообщения: {e.message}")
            await asyncio.sleep(10)

    last_updated_index = (last_updated_index + 1) % 14
    await save_post_ids(post_ids, last_updated_index)
  
def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('create_posts', create_initial_posts))
    app.add_handler(CommandHandler('create_main_post', create_main_post))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_and_reply))

    app.run_polling()

if __name__ == '__main__':
    main()
