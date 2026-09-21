import subprocess

subprocess.run([
    "powershell",
    "-Command",
    "[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]; "
    "$xml = New-Object Windows.Data.Xml.Dom.XmlDocument; "
    "$xml.LoadXml('<toast><visual><binding template=\"ToastText01\"><text>hey 2</text></binding></visual></toast>'); "
    "$toast = [Windows.UI.Notifications.ToastNotification]::new($xml); "
    "[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Python').Show($toast)"
])
