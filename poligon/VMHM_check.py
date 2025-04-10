from pathlib import Path
import asyncio

VM_path = Path(input('enter VM path: '))
HM_path = Path(input('enter HM path: '))

async def counter():
    vm_files = {f.name for f in VM_path.iterdir() if f.is_file()}
    hm_files = {f.name for f in HM_path.iterdir() if f.is_file()}

    for hm in vm_files:
        for vm in hm_files:
            if hm[2:]!=vm[2:]:
                print(hm)
                break

async def main():
    await counter()

if __name__ == "__main__":
    asyncio.run(main())