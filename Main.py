import base64

# اسکریپت انکود شده به صورت Base64
encoded_script = """
aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmZyb20gdXJsbGliLnBhcnNlIGltcG9ydCB1bnF1b3RlLCBwYXJzZV9xcywgdXJscGFyc2UKZnJvbSBsb2d1cnUgaW1wb3J0IGxvZ2dlcgppbXBvcnQgdGltZQppbXBvcnQgb3MKZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSwgU3R5bGUsIGluaXQKZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFRocmVhZFBvb2xFeGVjdXRvciwgYXNfY29tcGxldGVkCgojIEZ1bmN0aW9uIHRvIGNyZWF0ZSBhIGdyYWRpZW50IGZvciB0aGUgYmFubmVyCmRlZiBncmFkaWVudF9iYW5uZXIoKToKICAgICMgRGVmaW5lIGEgbW9yZSB2aWJyYW50IGNvbG9yIGdyYWRpZW50IChDeWFuLCBNYWdlbnRhLCBZZWxsb3csIEJsdWUsIEdyZWVuKQogICAgY29sb3JzID0gW0ZvcmUuQ1lBTiwgRm9yZS5NQUdFTlRBLCBGb3JlLllFTExPVywgRm9yZS5CTFVFLCBGb3JlLkdSRUVOXQogICAgCiAgICAjIEFTQ0lJIEJhbm5lciBsaW5lcwogICAgYmFubmVyX2xpbmVzID0gWwogICAgICAgICIrLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKyIsCiAgICAgICAgInwg4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojilojilojilZfilojilojilZcgICAg4paI4paI4paI4pWXICAg4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilZcgICAgIHwiLAogICAgICAgICJ84paI4paI4pWU4pWQ4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4pWa4pWQ4pWQ4paI4paI4pWU4pWQ4pWQ4pWd4paI4paI4pWRICAgIOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilZHilojilojilZTilZDilZDilojilojilZfilojilojilZEgICAgIHwiLAogICAgICAgICJ84paI4paI4pWRICAg4paI4paI4pWR4paI4paI4paI4paI4paI4paI4pWU4pWdICAg4paI4paI4pWRICAg4paI4paI4pWRICAgIOKWiOKWiOKVlOKWiOKWiOKWiOKWiOKVlOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKVkSAgICAgfCIsCiAgICAgICAgInzilojilojilZEgICDilojilojilZHilojilojilZTilZDilZDilZDilZ0gICAg4paI4paI4pWRICAg4paI4paI4pWRICAgIOKWiOKWiOKVkeKVmuKWiOKWiOKVlOKVneKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkeKWiOKWiOKVkSAgICAgfCIsCiAgICAgICAgInzilZrilojilojilojilojilojilojilZTilZ3ilojilojilZEgICAgICAgIOKWiOKWiOKVkSAgIOKWiOKWiOKVkSAgICDilojilojilZEg4pWa4pWQ4pWdIOKWiOKWiOKVkeKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4paI4paI4paI4paI4paI4pWXfCIsCiAgICAgICAgInwg4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWdIOKVmuKVkOKVnSAgICAgICAg4pWa4pWQ4pWdICAg4pWa4pWQ4pWdICAgIOKVmuKVkOKVnSAgICAg4pWa4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ3ilZrilZDilZDilZDilZDilZDilZDilZ18IiwKICAgICAgICAifCDilojilojilojilojilojilojilZcg4paI4paI4paI4paI4paI4paI4pWXICDilojilojilojilojilojilojilZcg4paI4paI4pWXICAgIOKWiOKWiOKVlyAgICDilojilojilZcgICDilojilojilZfilojilojilojilojilojilojilojilojilZcgIHwiLAogICAgICAgICJ84paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWdIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVkSAgICDilojilojilZEgICAg4pWa4paI4paI4pWXIOKWiOKWiOKVlOKVneKVmuKVkOKVkOKWiOKWiOKVlOKVkOKVkOKVnSAgfCIsCiAgICAgICAgInzilojilojilZEgIOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKVkSAgIOKWiOKWiOKVkeKWiOKWiOKVkSDilojilZcg4paI4paI4pWRICAgICDilZrilojilojilojilojilZTilZ0gICAg4paI4paI4pWRICAgICB8IiwKICAgICAgICAifOKWiOKWiOKVkSAgIOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVkSAgIOKWiOKWiOKVkeKWiOKWiOKVkeKWiOKWiOKWiOKVl+KWiOKWiOKVkSAgICAgIOKVmuKWiOKWiOKVlOKVnSAgICAg4paI4paI4pWRICAgICB8IiwKICAgICAgICAifOKVmuKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKVkSAg4paI4paI4pWR4pWa4paI4paI4paI4paI4paI4paI4pWU4pWd4pWa4paI4paI4paI4pWU4paI4paI4paI4pWU4pWdICAgICAgIOKWiOKWiOKVkSAgICAgIOKWiOKWiOKVkSAgICAgfCIsCiAgICAgICAgInwg4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWdIOKVmuKVkOKVnSAg4pWa4pWQ4pWdIOKVmuKVkOKVkOKVkOKVkOKVkOKVnSAg4pWa4pWQ4pWQ4pWd4pWa4pWQ4pWQ4pWdICAgICAgICDilZrilZDilZ0gICAgICDilZrilZDilZ0gICAgIHwiLAogICAgICAgICIrLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKyIKICAgIF0KICAgIAogICAgIyBQcmludCB0aGUgYmFubmVyIHdpdGggdGhlIGdyYWRpZW50IGVmZmVjdAogICAgZm9yIGksIGxpbmUgaW4gZW51bWVyYXRlKGJhbm5lcl9saW5lcyk6CiAgICAgICAgIyBDeWNsZSB0aHJvdWdoIHRoZSBjb2xvciBsaXN0IGZvciBlYWNoIGxpbmUKICAgICAgICBjb2xvciA9IGNvbG9yc1tpICUgbGVuKGNvbG9ycyldCiAgICAgICAgcHJpbnQoY29sb3IgKyBsaW5lKQoKIyBEZWZpbmUgaGVhZGVycyBnbG9iYWxseSBzbyBpdCdzIGFjY2Vzc2libGUgaW4gYWxsIGZ1bmN0aW9ucwpoZWFkZXJzID0gewogICAgJ2FjY2VwdCc6ICcqLyonLAogICAgJ2FjY2VwdC1sYW5ndWFnZSc6ICdlbixlbi1HQjtxPTAuOSxlbi1VUztxPTAuOCcsCiAgICAnYXV0aG9yaXphdGlvbic6ICcnLAogICAgJ2NhY2hlLWNvbnRyb2wnOiAnbm8tY2FjaGUnLAogICAgJ2NvbnRlbnQtdHlwZSc6ICdhcHBsaWNhdGlvbi9qc29uJywKICAgICdvcmlnaW4nOiAnaHR0cHM6Ly9ib3QudG9uY2lyY2xlLm9yZycsCiAgICAncHJhZ21hJzogJ25vLWNhY2hlJywKICAgICdwcmlvcml0eSc6ICd1PTEsIGknLAogICAgJ3JlZmVyZXInOiAnaHR0cHM6Ly9ib3QudG9uY2lyY2xlLm9yZy8nLAogICAgJ3gtcmVxdWVzdGVkLXdpdGgnOiAnb3JnLnRlbGVncmFtLm1lc3NlbmdlcicsCn0KCiMgRnVuY3Rpb24gdG8gbG9nIGEgbGluZSBzZXBhcmF0b3IKZGVmIGxvZ19saW5lKCk6CiAgICBwcmludChGb3JlLkdSRUVOICsgIj3imKA9IiAqIDIyICsgU3R5bGUuUkVTRVRfQUxMKQoKIyBNYWluIGZ1bmN0aW9uIHRvIHdhdGNoIGFuZCBwcm9jZXNzIHRoZSBnaXZlbiBzZXNzaW9uCmRlZiB3YXRjaChpbml0KToKICAgIHRnV2ViQXBwRGF0YSA9IHBhcnNlX3FzKHBhcnNlX3FzKHVybHBhcnNlKGluaXQpLmZyYWdtZW50KS5nZXQoJ3RnV2ViQXBwRGF0YScsIFtOb25lXSlbMF0pCiAgICB1c2VyX2RhdGEgPSB1bnF1b3RlKHRnV2ViQXBwRGF0YVsndXNlciddWzBdKQogICAgaWQgPSBqc29uLmxvYWRzKHVzZXJfZGF0YSlbJ2lkJ10KICAgIGNoYXRfaW5zdGFuY2UgPSB0Z1dlYkFwcERhdGFbJ2NoYXRfaW5zdGFuY2UnXVswXQogICAgcGFyYW1zID0gewogICAgICAgICdibG9ja0lkJzogJzM4NTInLAogICAgICAgICd0Z19pZCc6IHN0cihpZCksCiAgICAgICAgJ3RnX3BsYXRmb3JtJzogJ2FuZHJvaWQnLAogICAgICAgICdwbGF0Zm9ybSc6ICdMaW51eCBhcm02NCcsCiAgICAgICAgJ2xhbmd1YWdlJzogJ2VuJywKICAgICAgICAnY2hhdF90eXBlJzogJ3NlbmRlcicsCiAgICAgICAgJ2NoYXRfaW5zdGFuY2UnOiBjaGF0X2luc3RhbmNlLAogICAgfQogICAgZm9yIGkgaW4gcmFuZ2UoMSwgMTAwMDAwMDAwMDAwKToKICAgICAgICByZXNwb25zZSA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9hcGkuYWRzZ3JhbS5haS9hZHYnLCBwYXJhbXM9cGFyYW1zLCBoZWFkZXJzPWhlYWRlcnMpCiAgICAgICAgdHJhY2tpbmdfdmFsdWUgPSByZXNwb25zZS5qc29uKCkuZ2V0KCdiYW5uZXInLCB7fSkuZ2V0KCd0cmFja2luZ3MnLCBbXSkKICAgICAgICBpZiB0cmFja2luZ192YWx1ZSBhbmQgbGVuKHRyYWNraW5nX3ZhbHVlKSA+IDE6CiAgICAgICAgICAgIHRyYWNraW5nX3VybCA9IHRyYWNraW5nX3ZhbHVlWy0yXVsndmFsdWUnXQogICAgICAgICAgICByZXF1ZXN0cy5nZXQodHJhY2tpbmdfdXJsKQogICAgICAgICAgICBsb2dnZXIuaW5mbyhmJ3tpfSDwn5GMIDEwMDAgQ29pbnMgQ3JlZGl0ZWQgJykKICAgICAgICBlbHNlOgogICAgICAgICAgICBsb2dnZXIud2FybmluZygiTm8gdmFsaWQgdHJhY2tpbmcgZGF0YSBmb3VuZCIpCiAgICAgICAgCiAgICAgICAgIyBDb3VudGRvd24gdGltZXIgYmVmb3JlIHRoZSBuZXh0IHJlcXVlc3QgKDY1IHNlY29uZHMpCiAgICAgICAgZm9yIHQgaW4gcmFuZ2UoNjUsIDAsIC0xKToKICAgICAgICAgICAgcHJpbnQoRm9yZS5NQUdFTlRBICsgZiLRslBU0IfRqtCQ776aIEfQr9Gy0Kgg0KdUIHwgTmV4dCBwcm9jZXNzIHdpbGwgc3RhcnQgaW46IHt0fSBzZWNvbmRzLi4uIiwgZW5kPSJcciIpCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMSkgICMgU2xlZXAgZm9yIDEgc2Vjb25kCiAgICAgICAgbG9nZ2VyLmRlYnVnKCdzbGVlcGluZyA2NSBzZWNvbmRzIGZvciB0aGUgbmV4dCBBZCcpCgogICAgICAgICMgQ2FsbCB0aGUgbG9nX2xpbmUgZnVuY3Rpb24gdG8gcHJpbnQgdGhlIHNlcGFyYXRvciBhZnRlciBlYWNoIGxvb3AKICAgICAgICBsb2dfbGluZSgpCgojIFByaW50IHRoZSBiYW5uZXIKZGVmIGRpc3BsYXlfYmFubmVyKCk6CiAgICBncmFkaWVudF9iYW5uZXIoKSAgIyBDYWxsIHRoZSBncmFkaWVudF9iYW5uZXIgZnVuY3Rpb24gdG8gcHJpbnQgdGhlIGdyYWRpZW50IGJhbm5lcgogICAgcHJpbnQoRm9yZS5ZRUxMT1cgKyAiQ1JFQVRFRCBCWSA6IERSIEFCRFVMIE1BVElOIEtBUklNSTog4qitICIgKyBGb3JlLkdSRUVOICsgImh0dHBzOi8vdC5tZS9kb2N0b3JfYW1rIikKICAgIHByaW50KEZvcmUuV0hJVEUgKyAiRE9XTkxPQUQgTEFURVNUIEhBQ0tTIEhFUkUg4p6kICIgKyBGb3JlLkdSRUVOICsgImh0dHBzOi8vdC5tZS9vcHRpbWFsZ3Jvd1lUIikKICAgIHByaW50KEZvcmUuUkVEICsgIkxFQVJOIEhBQ0tJTkcgSEVSRSDinqQgIiArIEZvcmUuR1JFRU4gKyAiaHR0cHM6Ly93d3cueW91dHViZS5jb20vQG9wdGltYWxncm93WVQvdmlkZW9zIikKICAgIHByaW50KEZvcmUuUkVEICsgIkRPV05MT0FEIE1PUkUgSEFDS1Mg4p6kICIgKyBGb3JlLkdSRUVOICsgImh0dHBzOi8vZ2l0aHViLmNvbS9PcHRpbWFsR3Jvd1lUIikKICAgIHByaW50KEZvcmUuWUVMTE9XICsgIlBBU1RFIFlPVVIgW0xJTksgU0VTU0lPTl0gSU5UTyBUTElOS19TRVNTSU9OLlRYVCBGSUxFIEFORCBQUkVTUyBTVEFSVCAiKQogICAgcHJpbnQoRm9yZS5HUkVFTiArICLhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoDhmoBb8J2NlvCdjZbwnY2WIPCdmbLwnZqS8J2am/CdmozwnZqV8J2ajiDwnZm38J2ZsPCdmbLwnZm6IPCdmoXwnZm48J2ZvyDwnY2W8J2NlvCdjZZd4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqA4ZqAIikKCiMgSW5pdGlhbGl6ZSBjb2xvcmFtYQppbml0KGF1dG9yZXNldD1UcnVlKQoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKICAgICMgQ2xlYXIgdGhlIHNjcmVlbgogICAgb3Muc3lzdGVtKCdjbHMnIGlmIG9zLm5hbWUgPT0gJ250JyBlbHNlICdjbGVhcicpCiAgICAKICAgICMgRGlzcGxheSB0aGUgYmFubmVyIGFuZCBvdGhlciBpbmZvcm1hdGlvbgogICAgZGlzcGxheV9iYW5uZXIoKQoKICAgICMgQ2FsbCBsb2dfbGluZSB0byBwcmludCBzZXBhcmF0b3IgYWZ0ZXIgYmFubmVyCiAgICBsb2dfbGluZSgpCgogICAgIyBSZWFkIENpcmNsZSBzZXNzaW9uIGxpbmtzIGZyb20gJ0xpbmtfc2Vzc2lvbi50eHQnIGFuZCBwcm9jZXNzIHRoZW0KICAgIHRyeToKICAgICAgICB3aXRoIG9wZW4oJ0xpbmtfc2Vzc2lvbi50eHQnLCAncicpIGFzIGZpbGU6CiAgICAgICAgICAgIGxpbmtzID0gZmlsZS5yZWFkbGluZXMoKQogICAgICAgICAgICAjIFVzZSBUaHJlYWRQb29sRXhlY3V0b3IgdG8gcHJvY2VzcyBsaW5rcyBjb25jdXJyZW50bHkKICAgICAgICAgICAgd2l0aCBUaHJlYWRQb29sRXhlY3V0b3IobWF4X3dvcmtlcnM9MTApIGFzIGV4ZWN1dG9yOiAgIyBBZGp1c3QgdGhlIG1heF93b3JrZXJzIGFzIG5lZWRlZAogICAgICAgICAgICAgICAgZnV0dXJlcyA9IFtleGVjdXRvci5zdWJtaXQod2F0Y2gsIGxpbmsuc3RyaXAoKSkgZm9yIGxpbmsgaW4gbGlua3MgaWYgbGluay5zdHJpcCgpXQogICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAjIFdhaXQgZm9yIGFsbCBmdXR1cmVzIHRvIGNvbXBsZXRlCiAgICAgICAgICAgICAgICBmb3IgZnV0dXJlIGluIGFzX2NvbXBsZXRlZChmdXR1cmVzKToKICAgICAgICAgICAgICAgICAgICBmdXR1cmUucmVzdWx0KCkgICMgVGhpcyB3aWxsIHJhaXNlIGV4Y2VwdGlvbnMgaWYgYW55IG9jY3VyIGR1cmluZyBleGVjdXRpb24KICAgIGV4Y2VwdCBGaWxlTm90Rm91bmRFcnJvcjoKICAgICAgICBsb2dnZXIuZXJyb3IoIkxpbmtfc2Vzc2lvbi50eHQgZmlsZSBub3QgZm91bmQuIFBsZWFzZSBlbnN1cmUgdGhlIGZpbGUgZXhpc3RzLiIpCg==
"""

# دیکود کردن اسکریپت انکود شده
decoded_script = base64.b64decode(encoded_script).decode('utf-8')

# نمایش اسکریپت دیکود شده برای بررسی (اختیاری)
print("Decoded script:\n", decoded_script)

# اجرای اسکریپت دیکود شده
exec(decoded_script)
