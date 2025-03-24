import subprocess
import traceback

try:
    data = subprocess.check_output("netsh wlan show profiles").decode("cp866").split('\n')
    profiles = [el.split(":")[1][1:-1] for el in data if 'Все профили пользователей' in el]
    result_passwords = ''
    for profile in profiles:
        results = subprocess.check_output(
            ["netsh", "wlan", "show", "profiles", profile, "key=clear"]
        ).decode("cp866").split('\n')
        for result in results:
            if 'Содержимое ключа' in result:
                result_passwords += f"\t{profile}->{result.split(':')[1][1:-1]}\n"
    print(result_passwords)
except Exception as e:
    traceback.print_exc()