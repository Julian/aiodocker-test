from aiodocker import Docker, exceptions
import asyncio


async def main():
    docker = Docker()
    await docker.pull('ghcr.io/bowtie-json-schema/python-jsonschema',
                      tag='latest')
    container = await docker.containers.create(
        config={
            'Cmd': ['/bin/ash', '-c', 'echo "hello world"'],
            'Image': 'ghcr.io/bowtie-json-schema/python-jsonschema',
        },
        name='testing',
    )
    await container.start()
    logs = await container.log(stdout=True)
    print(''.join(logs))
    await container.delete(force=True)
    await docker.close()



asyncio.run(main())
