import os,psutil,AppOpener
def start():
    apps=[]
    imp_exe=['smss.exe', 'gui.exe', 'MpCmdRun.exe', 'WUDFHost.exe', 'TCPSVCS.EXE', 'audiodg.exe', 'wuauclt.exe', 'ShellExperienceHost.exe', 'OSPPSVC.EXE', ' audiodg.exe', 'WmiPrvSE.exe', 'MoUsoCoreWorker.exe', 'CompatTelRunner.exe', 'FileCoAuth.exe', 'ApplicationFrameHost.exe', 'TextInputHost.exe', 'python3.11.exe', 'SgrmBroker.exe', 'csrss.exe', 'svchost.exe', 'wininit.exe', 'winlogon.exe', 'services.exe', 'lsass.exe', 'dwm.exe', 'fontdrvhost.exe', 'taskhostw.exe', 'igfxCUIService.exe', 'sihost.exe', 'GoogleUpdate.exe', 'TranslucentTB.exe', 'mysqld.exe', 'dasHost.exe', 'ctfmon.exe', 'MsMpEng.exe', 'igfxEM.exe', 'igfxHK.exe', 'igfxTray.exe', 'msedge.exe', 'RuntimeBroker.exe', 'spoolsv.exe', 'conhost.exe', 'TiWorker.exe', 'explorer.exe', 'SearchFilterHost.exe', 'StartMenuExperienceHost.exe', 'wermgr.exe', 'TrustedInstaller.exe', 'SearchIndexer.exe', 'powershell.exe', 'SearchProtocolHost.exe', 'dllhost.exe', 'MicrosoftEdgeUpdate.exe', 'smartscreen.exe', 'NisSrv.exe', 'backgroundTaskHost.exe', 'SecurityHealthSystray.exe', 'SecurityHealthService.exe', 'GoogleCrashHandler.exe', 'GoogleCrashHandler64.exe', 'SearchApp.exe']
    AppOpener.close("msedge")
    AppOpener.close("file explorer")
    processes = psutil.process_iter()
    for i in processes:
        if i.name()!="Code.exe":
            if i.name().endswith(".exe") or i.name().endswith(".EXE"):
                if i.name() not in apps:
                    if i.name() not in imp_exe:
                        apps.append(i.name())
    for i in apps:
        os.system(f'cmd /c taskkill /F /IM {i}')