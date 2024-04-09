class ArgExtractor:
    def __init__(self, dataclass):
        self.dataclass = dataclass

    def extract(self, args):
        fields = self.dataclass.__dataclass_fields__
        return {field: args[field] for field in fields}
    
    def apply(self, args, fn):
        extracted = self.extract(args)
        return fn(**extracted)