import os
import pandas as pd
from mcp_server import MCPServer

# MCP 服務處理 Excel
class ExcelHandler:
    def __init__(self):
        self.file_path = "lab_data.xlsx"  # 你上傳的 Excel 檔案名

    def read_excel(self):
        df = pd.read_excel(self.file_path)
        return df.to_json()  # 轉成 JSON 給 AI 用

    def process_table(self, instructions):
        df = pd.read_excel(self.file_path)
        # 假設講義要求算平均值或整理表格
        if "平均值" in instructions:
            result = df.mean().to_dict()
        else:
            result = df.to_dict()
        return result

# 啟動 MCP 伺服器
server = MCPServer()
handler = ExcelHandler()
server.register_function("read_excel", handler.read_excel)
server.register_function("process_table", handler.process_table)

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8000)