from settings import get_token
from telegram.ext import (
    Updater, 
    CommandHandler,
    MessageHandler,
    Filters,
)
from handlers import (
    start,
    echo,
    ok,
    echo_photo,
    echo_audio,
    echo_video,
    echo_document,
    echo_dice,
    echo_animation,
    echo_contact,
    echo_location,
    til,
)

def main():
    try:
        TOKEN = get_token()
    except ValueError:
        print('400')
        return
    
    # create udpater obj
    updater = Updater(TOKEN)
    
    # create dispatcher obj
    dispatcher = updater.dispatcher
    
    # add command handlers
    dispatcher.add_handler(
        handler=CommandHandler(
            command=['start', 'boshlash'],
            callback=start
        )
    )
    
    # add message handlers
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('ok'),
            callback=ok
        )
    )
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("til"),callback=til))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text,callback=echo))
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.photo,
            callback=echo_photo
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.audio,
            callback=echo_audio,
            
        )
    )
    
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.video,
            callback=echo_video,
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.document,
            callback=echo_document,

        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.dice,
            callback=echo_dice,
            
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.animation,
            callback=echo_animation,
        )
    )

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.contact,
            callback=echo_contact,
        )
    )
    
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.location,
            callback=echo_location,
        )
    )
    # start polling
    updater.start_polling()
    updater.idle()

main()
