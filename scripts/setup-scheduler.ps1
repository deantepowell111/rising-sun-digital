# Setup scheduled task for Rising Sun Content Agent
$action = New-ScheduledTaskAction -Execute "python" -Argument '"c:\Users\alkal\Documents\official\scripts\content-agent.py" --generate' -WorkingDirectory "c:\Users\alkal\Documents\official\scripts"
$trigger = New-ScheduledTaskTrigger -Weekly -WeeksInterval 2 -DaysOfWeek Monday -At 9am
Register-ScheduledTask -TaskName "RisingSunContentAgent" -Action $action -Trigger $trigger -Description "Generate blog content ideas from Google Trends" -Force
Write-Host "Scheduled task created successfully!"
