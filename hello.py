from prefect import flow, task

@task
def create_message():
    msg = 'Hello from Prefect GitHub'
    return msg

@flow
def hello_world():
    task_message = create_message()
    print(task_message)

if __name__ == "__main__":
    hello_world()
