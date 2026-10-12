
import os
import discord
from discord.ext import commands
import yt_dlp

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"ALLESIA is online: {bot.user}")


    @bot.command()
    async def ping(ctx):
        await ctx.send("ALLESIA is here! 💜")


        @bot.command()
        async def join(ctx):
            if not ctx.author.voice:
                    await ctx.send("Join a voice channel first!")
                            return

                                channel = ctx.author.voice.channel

                                    if ctx.voice_client:
                                            await ctx.voice_client.move_to(channel)
                                                else:
                                                        await channel.connect()

                                                            await ctx.send("ALLESIA joined the voice! 🎧")


                                                            @bot.command()
                                                            async def leave(ctx):
                                                                if ctx.voice_client:
                                                                        await ctx.voice_client.disconnect()
                                                                                await ctx.send("ALLESIA left the voice.")
                                                                                    else:
                                                                                            await ctx.send("I'm not in a voice channel.")


                                                                                            @bot.command()
                                                                                            async def play(ctx, *, query: str):
                                                                                                if not ctx.author.voice:
                                                                                                        await ctx.send("Join a voice channel first!")
                                                                                                                return

                                                                                                                    if not ctx.voice_client:
                                                                                                                            await ctx.author.voice.channel.connect()

                                                                                                                                voice = ctx.voice_client

                                                                                                                                    if voice.is_playing():
                                                                                                                                            voice.stop()

                                                                                                                                                await ctx.send("Searching for audio... 🎵")

                                                                                                                                                    try:
                                                                                                                                                            options = {
                                                                                                                                                                        "format": "bestaudio/best",
                                                                                                                                                                                    "quiet": True,
                                                                                                                                                                                                "noplaylist": True,
                                                                                                                                                                                                        }

                                                                                                                                                                                                                with yt_dlp.YoutubeDL(options) as ydl:
                                                                                                                                                                                                                            info = ydl.extract_info(query, download=False)

                                                                                                                                                                                                                                    audio_url = info["url"]
                                                                                                                                                                                                                                            source = discord.FFmpegPCMAudio(
                                                                                                                                                                                                                                                        audio_url,
                                                                                                                                                                                                                                                                    before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                                                                                                                                                                                                                                                                                options="-vn"
                                                                                                                                                                                                                                                                                        )

                                                                                                                                                                                                                                                                                                voice.play(source)
                                                                                                                                                                                                                                                                                                        await ctx.send(f"Now playing: **{info.get('title', query)}** 🎶")

                                                                                                                                                                                                                                                                                                            except Exception:
                                                                                                                                                                                                                                                                                                                    await ctx.send("Couldn't play this audio. Try another URL.")


                                                                                                                                                                                                                                                                                                                    @bot.command()
                                                                                                                                                                                                                                                                                                                    async def stop(ctx):
                                                                                                                                                                                                                                                                                                                        if ctx.voice_client and ctx.voice_client.is_playing():
                                                                                                                                                                                                                                                                                                                                ctx.voice_client.stop()
                                                                                                                                                                                                                                                                                                                                        await ctx.send("Music stopped. ⏹️")


                                                                                                                                                                                                                                                                                                                                        @bot.command()
                                                                                                                                                                                                                                                                                                                                        async def pause(ctx):
                                                                                                                                                                                                                                                                                                                                            if ctx.voice_client and ctx.voice_client.is_playing():
                                                                                                                                                                                                                                                                                                                                                    ctx.voice_client.pause()
                                                                                                                                                                                                                                                                                                                                                            await ctx.send("Music paused. ⏸️")


                                                                                                                                                                                                                                                                                                                                                            @bot.command()
                                                                                                                                                                                                                                                                                                                                                            async def resume(ctx):
                                                                                                                                                                                                                                                                                                                                                                if ctx.voice_client and ctx.voice_client.is_paused():
                                                                                                                                                                                                                                                                                                                                                                        ctx.voice_client.resume()
                                                                                                                                                                                                                                                                                                                                                                                await ctx.send("Music resumed. ▶️")


                                                                                                                                                                                                                                                                                                                                                                                token = os.getenv("DISCORD_TOKEN")

                                                                                                                                                                                                                                                                                                                                                                                if not token:
                                                                                                                                                                                                                                                                                                                                                                                    raise RuntimeError("Please configure the DISCORD_TOKEN environment variable.")

                                                                                                                                                                                                                                                                                                                                                                                    bot.run(token)
                                                                                                                                                                                                                                                                                                                                                                                    