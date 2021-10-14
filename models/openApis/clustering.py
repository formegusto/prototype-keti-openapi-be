from common.mongo_connect import conn_mongodb


class CLUSTERING():
    @staticmethod
    def find(page=1, offset=10):
        col = conn_mongodb().keti_pattern_recognition.cluster_info
        clustering_cur = col.find().limit(10)
        clustering = list()

        for _ in clustering_cur:
            _['id'] = str(_['_id'])
            del _['_id']

            clustering.append(_)

        return clustering
