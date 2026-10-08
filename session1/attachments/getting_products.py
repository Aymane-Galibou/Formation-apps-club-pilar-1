
from functools import wraps
import time
import requests
import asyncio

back_end_api = 'dir api dyalk hnaya asaaaaaaaaahbi'

def retry(n_time,wait_duration):
    def decorator(func):
        async def wrapper(*args,**kwargs):
            for _ in range(1,n_time+1):
                try:
                    return await func(*args,**kwargs)
                except Exception as e:
                    print(f'The problem is {e}')
                    await asyncio.sleep(wait_duration)
        return wrapper

    return decorator

@retry(3,4)
async def get_products():
    response = requests.get(back_end_api)
    return response.json()




async def main():
    print("Fetching products...")
    try:
        # bash tjreb failure dir xi api ghalat
        data = await get_products()
        print(
            f"Successfully fetched! Total products: {len(data.get('data', []))}"
        )
    except Exception as e:
        print("Final error caught in main.")


# Entry point
if __name__ == "__main__":
    asyncio.run(main())