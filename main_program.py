import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def send_daily_report():
    # 邮件配置
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.example.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    SMTP_USERNAME = os.getenv('SMTP_USERNAME', 'your_email@example.com')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', 'your_password')
    
    FROM_EMAIL = os.getenv('FROM_EMAIL', 'your_email@example.com')
    TO_EMAILS = os.getenv('TO_EMAILS', 'recipient1@example.com,recipient2@example.com').split(',')
    
    # 获取当前日期
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 创建邮件内容
    subject = f"每日工作报告 - {today}"
    
    # HTML 格式的报告内容
    html_content = f"""
    <html>
        <body>
            <h1>每日工作报告 - {today}</h1>
            <p>尊敬的团队，</p>
            
            <h2>1. 今日总结</h2>
            <ul>
                <li>项目A: 完成进度80%</li>
                <li>项目B: 需求分析完成</li>
                <li>项目C: 测试通过</li>
            </ul>
            
            <h2>2. 明日计划</h2>
            <ul>
                <li>项目A: 完成剩余20%</li>
                <li>项目B: 开始开发</li>
                <li>项目D: 需求讨论</li>
            </ul>
            
            <h2>3. 问题与障碍</h2>
            <ul>
                <li>服务器偶尔出现延迟</li>
                <li>需要更多设计资源</li>
            </ul>
            
            <p>祝好，<br/>
            你的团队</p>
            
            <p><small>此邮件为自动发送，请勿直接回复。</small></p>
        </body>
    </html>
    """
    
    # 纯文本版本（用于不支持HTML的客户端）
    text_content = f"""
    每日工作报告 - {today}
    
    尊敬的团队，
    
    1. 今日总结
    - 项目A: 完成进度80%
    - 项目B: 需求分析完成
    - 项目C: 测试通过
    
    2. 明日计划
    - 项目A: 完成剩余20%
    - 项目B: 开始开发
    - 项目D: 需求讨论
    
    3. 问题与障碍
    - 服务器偶尔出现延迟
    - 需要更多设计资源
    
    祝好，
    你的团队
    
    此邮件为自动发送，请勿直接回复。
    """
    
    # 创建邮件消息
    msg = MIMEMultipart('alternative')
    msg['From'] = FROM_EMAIL
    msg['To'] = ', '.join(TO_EMAILS)
    msg['Subject'] = subject
    
    # 添加文本和HTML版本
    part1 = MIMEText(text_content, 'plain')
    part2 = MIMEText(html_content, 'html')
    
    msg.attach(part1)
    msg.attach(part2)
    
    try:
        # 连接SMTP服务器并发送邮件
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAILS, msg.as_string())
        server.quit()
        print(f"邮件发送成功！时间: {datetime.now()}")
    except Exception as e:
        print(f"邮件发送失败: {str(e)}")

if __name__ == "__main__":
    send_daily_report()
