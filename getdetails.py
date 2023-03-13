import asyncio, json, time, os
from winrt.windows.storage.streams import \
    DataReader, Buffer, InputStreamOptions
from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager
while True:
    async def get_media_info():
        sessions = await MediaManager.request_async()
        current_session = sessions.get_current_session()
        if current_session:
            info = await current_session.try_get_media_properties_async()

            info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}

            info_dict['genres'] = list(info_dict['genres'])

            return info_dict
    try:
        if __name__ == '__main__':
            current_media_info = asyncio.run(get_media_info())

        if current_media_info == None:
            continue

        async def read_stream_into_buffer(stream_ref, buffer):
            readable_stream = await stream_ref.open_read_async()
            readable_stream.read_async(buffer, buffer.capacity, InputStreamOptions.READ_AHEAD)


        # create the current_media_info dict with the earlier code first
        thumb_stream_ref = current_media_info['thumbnail']

        # 5MB (5 million byte) buffer - thumbnail unlikely to be larger
        thumb_read_buffer = Buffer(5000000)

        # copies data from data stream reference into buffer created above
        asyncio.run(read_stream_into_buffer(thumb_stream_ref, thumb_read_buffer))

        # reads data (as bytes) from buffer
        buffer_reader = DataReader.from_buffer(thumb_read_buffer)
        byte_buffer = buffer_reader.read_bytes(thumb_read_buffer.length)

        #pop dict as it breaks dict
        current_media_info.pop('thumbnail')
        with open('media_thumb.png', 'wb+') as fobj:
            fobj.write(bytearray(byte_buffer))

        with open('info.json', 'w+', encoding = 'utf-8') as wdict:
            json.dump(current_media_info, wdict)
        time.sleep(0.5)
    except NameError:
        print("Error")
        continue