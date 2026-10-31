elif choice == '7':
            token = generate_api_token()
            beep()
            print(f"\n{GREEN}[+] API Token: {YELLOW}{token}{RESET}")
            if copy_to_clipboard(token): print(f"{CYAN}[i] Скопировано{RESET}")
            ans = input(f"\n{CYAN}[?] Сохранить? (y/n): {RESET}").lower()
            if ans == 'y': save_password(token, "API-Key")
            else: SESSION_HISTORY.append(token)
            input(f"\n{CYAN}Enter...{RESET}")

        elif choice == '8':
            beep()
            print(f"\n{GREEN}[+] UUID: {YELLOW}{generate_uuid()}{RESET}")
            input(f"\n{CYAN}Enter...{RESET}")

        elif choice == '9':
            pwd = input(f"{CYAN}Введите пароль: {RESET}")
            beep()
            print(f"\n{CYAN}[i] Надежность: {check_strength(pwd)}{RESET}")
            input(f"\n{CYAN}Enter...{RESET}")

        elif choice == '10':
            pwd = input(f"{CYAN}Введите текст: {RESET}")
            beep()
            print(f"\n{GREEN}[+] SHA-256: {YELLOW}{hashlib.sha256(pwd.encode()).hexdigest()}{RESET}")
            input(f"\n{CYAN}Enter...{RESET}")

        elif choice == '11':
            clear()
            top_menu()
            print(f"{YELLOW}--- СОХРАНЕННЫЕ ДАННЫЕ ---{RESET}\n")
            if os.path.exists(DB_FILE):
                with open(DB_FILE, "r") as file:
                    print(file.read())
            else:
                print(f"{RED}Файл пуст.{RESET}")
            input(f"\n{CYAN}Enter...{RESET}")

        elif choice == '12':
            if os.path.exists(DB_FILE):
                import shutil
                shutil.copy(DB_FILE, "export_backup.txt")
                beep()
                print(f"\n{GREEN}[+] Экспорт в export_backup.txt выполнен.{RESET}")
            input(f"\n{CYAN}Enter...{RESET}")

        elif choice == '13':
            print(f"\n{YELLOW}[*] Проверка сети (Ping)...{RESET}")
            start = time.time()
            try:
                requests.get("https://google.com", timeout=3)
                ping = int((time.time() - start) * 1000)
                beep()
                print(f"{GREEN}[+] Пинг: {ping} ms{RESET}")
            except:
                print(f"{RED}[-] Сеть недоступна.{RESET}")
            input(f"\n{CYAN}Enter...{RESET}")

        elif choice == '14':
            print(f"\n{CYAN}[i] Канал: {YELLOW}t.me/your_tg{RESET}")
            time.sleep(1.5)

        else:
            beep()
            print(f"{RED}[-] Неизвестная команда.{RESET}")
            time.sleep(1)

if name == "main":
    main()
