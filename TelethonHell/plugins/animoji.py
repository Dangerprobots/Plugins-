import asyncio
from collections import deque

from TelethonHell.plugins import *


@hell_cmd(pattern="think$")
async def _(event):
    event = await eor(event, "think")
    deq = deque(list("π€π§π€π§π€π§"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@hell_cmd(pattern="ccry$")
async def cry(e):
    await eor(e, "(;Β΄ΰΌΰΊΆΠΰΌΰΊΆ)")


@hell_cmd(pattern="fap$")
async def _(event):
    event = await eor(event, "fapping(Β°_Β°)")
    deq = deque(list("πβπ»π¦"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@hell_cmd(pattern="lmao$")
async def _(event):
    event = await eor(event, "lmao")
    deq = deque(list("ππ€£ππ€£ππ€£"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@hell_cmd(pattern="nothappy$")
async def _(event):
    event = await eor(event, "nathappy")
    deq = deque(list("πβΉοΈπβΉοΈπβΉοΈπ"))
    for _ in range(48):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)


@hell_cmd(pattern="clock$")
async def _(event):
    event = await eor(event, "clock")
    deq = deque(list("πππππππππππ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@hell_cmd(pattern="muah$")
async def _(event):
    event = await eor(event, "muah")
    deq = deque(list("πππππ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@hell_cmd(pattern="heart$")
async def _(event):
    event = await eor(event, "heart")
    deq = deque(list("β€οΈπ§‘πππππ€"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@hell_cmd(pattern="gym$")
async def _(event):
    event = await eor(event, "gym")
    deq = deque(list("πβπβπ€Έβπβπβπ€Έβπβπβπ€Έβ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@hell_cmd(pattern="earth$")
async def _(event):
    event = await eor(event, "earth")
    deq = deque(list("ππππππππ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@hell_cmd(pattern="moon$")
async def _(event):
    event = await eor(event, "moon")
    deq = deque(list("ππππππππ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@hell_cmd(pattern="lovestory$")
async def _(event):
    animation_interval = 3
    animation_ttl = range(0, 103)
    await eor(event, "Let me tel you")
    animation_chars = [
        "1 β€οΈ love story",
        "  π             π \n/π\         <π\ \n π               /|",
        "  π          π³ \n/π\       /π\ \n  π            /|",
        "  π            π \n/π\         <π> \n  π             /|",
        "  π         βΊοΈ \n/π\      /π\ \n  π          /|",
        "  π          π \n/π\       /π\ \n  π           /|",
        "  π   π \n /π\/π\ \n   π   /|",
        " π³  π \n /|\ /π\ \n /     / |",
        "π    /π°\ \n<|\      π \n /π    / |",
        "π \n/(),βπ? \n /\         _/\\/|",
        "π \n/\\_,__π« \n  //    //       \\",
        "π \n/\\_,π¦_π  \n  //         //        \\",
        "  π­      βΊοΈ \n  /|\   /(πΆ)\ \n  /!\   / \ ",
        "Abee aur kitna dekhoge be besharmi ki bhi hadd hoti hai..,The End π...",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 103])


@hell_cmd(pattern="smoon$")
async def _(event):
    event = await eor(event, "smoon")
    animation_interval = 0.1
    animation_ttl = range(101)
    await event.edit("smoon..")
    animation_chars = [
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
        "πππππ\nπππππ\nπππππ\nπππππ\nπππππ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@hell_cmd(pattern="tmoon$")
async def _(event):
    event = await eor(event, "tmoon")
    animation_interval = 0.1
    animation_ttl = range(117)
    await event.edit("tmoon")
    animation_chars = [
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
        "π",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


@hell_cmd(pattern="hart$")
async def _(event):
    animation_interval = 0.5
    animation_ttl = range(20)
    event = await eor(event, "β€οΈ")
    animation_chars = ["π€", "β€οΈ", "π€", "β€οΈ", "β"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@hell_cmd(pattern="anim$")
async def _(event):
    animation_interval = 1
    animation_ttl = range(20)
    event = await eor(event, "π’")
    animation_chars = [
        "π",
        "π§",
        "π‘",
        "π’",
        "π",
        "π§",
        "π‘",
        "π’",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@hell_cmd(pattern="fuck$")
async def _(event):
    animation_interval = 1
    animation_ttl = range(0, 101)
    await eor(event, "fuk")
    animation_chars = ["π       βοΈ", "π     βοΈ", "π  βοΈ", "πβοΈπ¦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@hell_cmd(pattern="sux$")
async def _(event):
    animation_interval = 1
    animation_ttl = range(0, 101)
    await eor(event, "sux")
    animation_chars = ["π€΅       π°", "π€΅     π°", "π€΅  π°", "π€΅πΌπ°"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@hell_cmd(pattern="kiss$")
async def _(event):
    animation_interval = 1
    animation_ttl = range(0, 101)
    await eor(event, "kiss")
    animation_chars = ["π€΅       π°", "π€΅     π°", "π€΅  π°", "π€΅ππ°"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@hell_cmd(pattern="fnl$")
async def _(event):
    animation_interval = 2
    animation_ttl = range(6)
    event = await eor(event, "Hey There....")
    animation_chars = ["ππΏ", "ππΎ", "ππ½", "ππΌ", "βπ"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@hell_cmd(pattern="monkey$")
async def _(event):
    animation_interval = 2
    animation_ttl = range(12)
    event = await eor(event, "Hey There....")
    animation_chars = ["π΅", "π", "π", "π", "πβπ΅π"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@hell_cmd(pattern="hand$")
async def _(event):
    animation_interval = 1
    animation_ttl = range(13)
    event = await eor(event, "ποΈ")
    animation_chars = [
        "π",
        "π",
        "βοΈ",
        "π",
        "π",
        "π",
        "βοΈ",
        "π€",
        "π",
        "π€",
        "π€",
        "ποΈ",
        "π",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])


@hell_cmd(pattern="gsg$")
async def _(event):
    animation_interval = 1
    animation_ttl = range(12)
    event = await eor(event, "ContDown....")
    animation_chars = [
        "π",
        "9οΈβ£",
        "8οΈβ£",
        "7οΈβ£",
        "6οΈβ£",
        "5οΈβ£",
        "4οΈβ£",
        "3οΈβ£",
        "2οΈβ£",
        "1οΈβ£",
        "0οΈβ£",
        "π",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@hell_cmd(pattern="theart$")
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await eor(event, "π€")
    animation_chars = [
        "β€οΈ",
        "π§‘",
        "π",
        "π",
        "π",
        "π",
        "π€",
        "π",
        "π",
        "β€οΈ",
        "π§‘",
        "π",
        "π",
        "π",
        "π",
        "π€",
        "π",
        "π",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


CmdHelp("animoji").add_command(
    "think", None, "Use and see"
).add_command(
    "ccry", None, "Use and see"
).add_command(
    "fap", None, "Use and see"
).add_command(
    "lmao", None, "Use and see"
).add_command(
    "nothappy", None, "Use and see"
).add_command(
    "clock", None, "Use and see"
).add_command(
    "muah", None, "Use and see"
).add_command(
    "heart", None, "Use and see"
).add_command(
    "gym", None, "Use and see"
).add_command(
    "earth", None, "Use and see"
).add_command(
    "moon", None, "Use and see"
).add_command(
    "lovestory", None, "Turu Lob"
).add_command(
    "smoon", None, "Use and see"
).add_command(
    "tmoon", None, "Use and see"
).add_command(
    "hart", None, "Use and see"
).add_command(
    "anim", None, "Use and see"
).add_command(
    "fuck", None, "Use and see"
).add_command(
    "sux", None, "Use and see"
).add_command(
    "kiss", None, "Kya dekh rha h jhopdike."
).add_command(
    "fnl", None, "Use and See."
).add_command(
    "monkey", None, "Use and see."
).add_command(
    "hand", None, "Use and See."
).add_command(
    "gsg", None, "Use and See."
).add_command(
    "theart", None, "Hearts Animation."
).add()
