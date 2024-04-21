from asgiref.sync import sync_to_async


class ToplivoPipeline:

    @sync_to_async
    def process_item(self, item, spider):
        item.save()
        return item
