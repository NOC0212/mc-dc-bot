# 🎮 Minecraft 基岩版伺服器狀態 Discord 機器人
## 這個 Discord 機器人用於監控您的 Minecraft 基岩版 (Bedrock Edition) 伺服器狀態，並將即時的玩家數量和校準後的延遲數據顯示為機器人的自訂狀態。
## ✨ 主要功能
 * 實時伺服器監控：定時查詢 Minecraft 基岩版伺服器狀態。
 * 動態活動狀態：將伺服器上的玩家數量（例如：玩家: 8/50）和校準後的延遲（例如：延遲: 123ms）顯示為 Discord 機器人的自訂活動狀態。
 * 自動在線/離線檢測：當伺服器離線或查詢超時時，機器人狀態會自動更新為「伺服器離線或超時」。
 * 手動查詢指令：提供 !mcbestatus 指令，允許用戶隨時手動查詢伺服器詳細狀態。
 * 自訂延遲校準：延遲數據會經過 (原始延遲 / 2) - 18 的公式計算後顯示，以更好地符合特定地理區域的實際體驗。
 * 避免 Discord API 限速：更新頻率經過優化，以確保機器人狀態更新不會觸發 Discord API 的限速。
## 🚀 開始使用
在運行此機器人之前，請確保您具備以下條件：
 * Python 3.8+ 環境
 * Discord 機器人帳戶：您需要一個 Discord 機器人應用程式和其 Bot Token。
   * 前往 Discord Developers Portal。
   * 創建一個新的應用程式。
   * 在應用程式設定中導航到 Bot 選項卡，並生成一個新的 Token。請妥善保管此 Token，切勿公開！
   * 確保您的機器人在 OAuth2 -> URL Generator 中至少擁有 bot 權限，並且在 Bot 選項卡中啟用 Message Content Intent。
 * Discord 伺服器：將您的機器人邀請到您要監控的 Discord 伺服器中。
 * Minecraft 基岩版伺服器：確保您擁有一個正在運行的 Minecraft 基岩版伺服器 (IP 和埠號)。
## 安裝步驟
 * 複製儲存庫：
   git clone https://github.com/NOC0212/mc-dc-bot.git
cd mc-dc-bot

 * 安裝必要的 Python 函式庫：
   pip install discord.py mcstatus asyncio

 * 配置機器人：
   打開 main.py (或您儲存程式碼的檔案)，並修改頂部的配置區塊：
   ### --- 配置您的資訊 ---
* MINECRAFT_SERVER_ADDRESS = "您的Minecraft伺服器IP或域名" # 例如: "20.195.24.81"
* MINECRAFT_SERVER_PORT = 您的Minecraft伺服器埠號 # 例如: 24572 或預設的 19132
* DISCORD_BOT_TOKEN = "您的Discord機器人權杖" # 將這裡替換為您的機器人Token

## 自動更新的間隔時間 (秒)
## 推薦 5-20 秒，以實現較快的更新同時避免限速
UPDATE_INTERVAL_SECONDS = 5
# --- 配置結束 ---

   * 將 MINECRAFT_SERVER_ADDRESS 和 MINECRAFT_SERVER_PORT 替換為您的伺服器資訊。
   * 將 DISCORD_BOT_TOKEN 替換為您從 Discord Developers Portal 獲取到的機器人 Token。
   * UPDATE_INTERVAL_SECONDS 預設為 30 秒，您可以根據需要調整，但請勿設置過低以避免潛在的 Discord API 限速。
 ## 運行機器人：
   python main.py
   如果一切配置正確，您將在控制台中看到「機器人已準備好！」的訊息，並且機器人會開始更新其狀態。
🔧 配置選項說明
 * MINECRAFT_SERVER_ADDRESS: 您的 Minecraft 基岩版伺服器的 IP 位址或域名。
 * MINECRAFT_SERVER_PORT: 您的 Minecraft 基岩版伺服器的埠號。
 * DISCORD_BOT_TOKEN: 您的 Discord 機器人的驗證權杖。
 * UPDATE_INTERVAL_SECONDS: 機器人自動更新其狀態的間隔時間（以秒為單位）。
📝 使用方式
機器人運行後，它會自動開始監控伺服器狀態並更新自己的活動狀態。
 * 機器人狀態顯示：
   * 在 Discord 伺服器的成員列表中，您會看到機器人名稱下方顯示類似 玩家: 8/50 | 延遲: 123ms 的狀態。
   * 如果伺服器離線或無法訪問，狀態會顯示 🔴 伺服器離線或超時。
   * 如果機器人在查詢時遇到其他錯誤，會顯示 🟠 伺服器錯誤 (錯誤類型)。
 * 手動查詢指令：
   * 在任何有機器人的文字頻道中輸入 !mcbestatus，機器人會發送一個嵌入式訊息，顯示當前的伺服器詳細狀態。
💡 延遲校準說明
程式碼中的延遲計算公式 (原始延遲 / 2) - 18 是為了校準或估計一個更貼近實際玩家連接到伺服器時的延遲。由於機器人的託管位置（例如英國）與您的 Minecraft 伺服器位置（例如東南亞）可能存在地理差異，機器人測量的原始延遲可能與您在遊戲中感受到的延遲不同。此公式旨在彌補這種地理差異帶來的影響。
⚠️ 常見問題與故障排除
 * 機器人沒有上線：
   * 檢查 DISCORD_BOT_TOKEN 是否正確。
   * 確保您的網絡連接穩定。
   * 檢查控制台是否有 LoginFailure 錯誤。
 * 機器人狀態沒有更新：
   * 檢查控制台是否有任何錯誤訊息，特別是與 mcstatus 查詢相關的錯誤。
   * 確認 MINECRAFT_SERVER_ADDRESS 和 MINECRAFT_SERVER_PORT 是否正確。
   * 確保 Minecraft 伺服器正在運行並且可以從外部訪問。
 * Discord API 限速警告：
   * 如果控制台出現 We are being rate limited 警告，這表示您可能將 UPDATE_INTERVAL_SECONDS 設置得太低。嘗試增加該值（例如，從 30 秒增加到 60 秒或 120 秒）。對於機器人活動狀態，30 秒通常是安全的。
 * 玩家人數顯示 N/A：
   * 這可能意味著 mcstatus 函式庫無法從您的 Minecraft 伺服器獲取到玩家列表信息。這可能是伺服器配置、版本不兼容或 mcstatus 函式庫的局限性所致。此時，機器人會顯示 N/A。
🤝 貢獻
歡迎任何形式的貢獻！如果您有任何改進建議、Bug 報告或新功能請求，請隨時提交 Pull Request 或開啟 Issue。
📄 許可證
此專案採用 MIT 許可證。詳情請見 LICENSE 檔案。
請記得將 您的用戶名/您的儲存庫名稱 替換為您 GitHub 專案的實際路徑。
如果您沒有 LICENSE 檔案，可以將「許可證」部分移除。
