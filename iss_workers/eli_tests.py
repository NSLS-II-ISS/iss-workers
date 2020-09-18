def react(consumer,topic, name, doc):
    if name=='start':
        print(name + " Josh is great " + doc['uid'])
        
bsc = BlueskyConsumer(topics = ["iss.bluesky.documents"],bootstrap_servers='cmb01:9092,cmb02:9092,cmb03:9092',
group_id='iss',
consumer_config={ "auto.offset.reset": "latest"},
process_document=react
)


bsc.start()
