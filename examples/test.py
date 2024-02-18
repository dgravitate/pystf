import sys

from stf.base import BaseTransform
from stf.transformers import XMLTransform


with open(sys.argv[1], "r") as f:
    transformer = BaseTransform.get_transformer_for_type(f.read(), delimiter="/")
    base_path = "MESSAGE/DOCUMENT_SETS/DOCUMENT_SET/DOCUMENTS/DOCUMENT"
    application_number = transformer.select(f"{base_path}/DEAL_SETS/DEAL_SET/DEALS/DEAL/EXTENSION/OTHER/cl:DEAL/cl:KEYS/cl:KEY", 'cl:KeyIdentifier == "loanNumber"', "cl:KeyValue", coerce_to_string=True)
    status = transformer.extract(f"{base_path}/DEAL_SETS/DEAL_SET/DEALS/DEAL/SERVICES/SERVICE/STATUSES/STATUS/StatusCode")

    print(application_number, status)
