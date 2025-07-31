import discord
from discord.ext import commands, tasks
import asyncio
from mcstatus.server import BedrockServer

# --- 配置您的資訊 ---(-------修改處-------)
MINECRAFT_SERVER_ADDRESS = "YOUR_SERVER_IP"
MINECRAFT_SERVER_PORT = YOUR_SERVER_PORT
DISCORD_BOT_TOKEN = "YOUR_DISCORDBOT_TOKEN"

# 自動更新的間隔時間 (秒)(-------修改處-------)
UPDATE_INTERVAL_SECONDS = 5 

# --- 配置結束 ---

# 設定 Discord 機器人的指令前綴和意圖
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'已成功登入為 {bot.user.name} ({bot.user.id})')
    print('機器人已準備好！')
    update_bot_status.start()

@tasks.loop(seconds=UPDATE_INTERVAL_SECONDS)
async def update_bot_status():
    try:
        server = BedrockServer(MINECRAFT_SERVER_ADDRESS, MINECRAFT_SERVER_PORT) 
        status = await asyncio.wait_for(server.async_status(), timeout=10) 
        
        # 打印語句以診斷玩家數據 (保持不變)
        print(f"--- 伺服器狀態查詢結果 ---")
        print(f"MCBE Status Object: {status}")
        print(f"Players Object: {getattr(status, 'players', 'N/A_AttributeNotFound')}")
        if hasattr(status, 'players') and status.players is not None:
            print(f"Online Players: {status.players.online}, Max Players: {status.players.max}")
        else:
            print(f"玩家資訊無法獲取或為空。")
        print(f"--------------------------")

        online_players = getattr(status.players, 'online', 'N/A') if getattr(status, 'players', None) else 'N/A'
        max_players = getattr(status.players, 'max', 'N/A') if getattr(status, 'players', None) else 'N/A'
        latency_value = round(status.latency) if hasattr(status, 'latency') else 'N/A'

        # 設定機器人的自訂狀態
        activity_message = f"玩家: {online_players}/{max_players} | 延遲: {latency_value}ms"
        
        await bot.change_presence(activity=discord.CustomActivity(name=activity_message))
        print(f"機器人狀態已更新為: {activity_message}")

    except asyncio.TimeoutError:
        offline_message = "🔴 伺服器離線或超時"
        await bot.change_presence(activity=discord.CustomActivity(name=offline_message))
        print(f"機器人狀態已更新為: {offline_message}")

    except Exception as e:
        print(f"查詢伺服器或更新機器人狀態時發生錯誤: {e}") 
        error_message = f"🟠 伺服器錯誤 ({e.__class__.__name__})"
        await bot.change_presence(activity=discord.CustomActivity(name=error_message))
        print(f"機器人狀態已更新為: {error_message}")

        
# 監測 Minecraft 基岩版伺服器狀態的指令 (手動查詢功能保留)
@bot.command(name='mcbestatus', help='檢查 Minecraft 基岩版伺服器狀態')
async def mcbestatus(ctx):
    """
    發送此指令後，機器人將嘗試連接到指定的 Minecraft 基岩版伺服器並顯示其狀態。
    """
    await ctx.send("正在查詢 Minecraft 基岩版伺服器狀態，請稍候...")
    try:
        server = BedrockServer(MINECRAFT_SERVER_ADDRESS, MINECRAFT_SERVER_PORT) 
        status = await asyncio.wait_for(server.async_status(), timeout=10) 

        embed = discord.Embed(
            title=f"Minecraft 基岩版伺服器狀態：{MINECRAFT_SERVER_ADDRESS}",
            color=discord.Color.green() 
        )
        embed.add_field(name="狀態", value="🟢 線上", inline=True)
        embed.add_field(name="版本", value=status.version.name, inline=True)
        
        online_players = getattr(status.players, 'online', 'N/A') if getattr(status, 'players', None) else 'N/A'
        max_players = getattr(status.players, 'max', 'N/A') if getattr(status, 'players', None) else 'N/A'
        embed.add_field(name="玩家", value=f"{online_players}/{max_players}", inline=True)
        
        embed.add_field(name="MOTD", value=status.description, inline=False)
        embed.add_field(name="延遲", value=f"{round(status.latency)} ms", inline=True)

        await ctx.send(embed=embed)

    except asyncio.TimeoutError:
        embed = discord.Embed(
            title=f"Minecraft 基岩版伺服器狀態：{MINECRAFT_SERVER_ADDRESS}",
            description="🔴 伺服器查詢超時，可能離線或無法訪問。",
            color=discord.Color.orange() 
        )
        await ctx.send(embed=embed)
    except Exception as e:
        print(f"查詢伺服器時發生錯誤: {e}") 
        embed = discord.Embed(
            title=f"Minecraft 基岩版伺服器狀態：{MINECRAFT_SERVER_ADDRESS}",
            description=f"🔴 離線 或發生錯誤：`{e}`",
            color=discord.Color.red() 
        )
        await ctx.send(embed=embed)

try:
    bot.run(DISCORD_BOT_TOKEN)
except discord.LoginFailure:
    print("\n錯誤：Discord 機器人權杖無效！請檢查 DISCORD_BOT_TOKEN 是否正確。")
except Exception as e:
    print(f"\n機器人運行時發生未知錯誤：{e}")
