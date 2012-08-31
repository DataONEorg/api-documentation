@startuml images/morpho-class-diagram.png

class D1Object {
- DataStore[] dataStoreList
+ D1Object(Identifier identifier, DataStore[] dataStoreList)
+ Identifier getIdentifier()
+ void setIdentifier(Identifier identifier)
+ ObjectFormatIdentifier getFormatId()
+ OutputStream getData()
+ SystemMetadata getSystemMetadata()
+ void setData(InputStream input)
+ void setSystemMetadata(SystemMetadata systemMetadata)
+ Identifier getPreviousIdentifier()
+ void setPreviousIdentifier(Identifier previousIdentifier)
+ void registerDataStore(DataStore dataStore)
+ void  removeDataStore(DataStore dataStore)
+ DataStore[] getDataStoreIDList()
}

class Entity {
- Node entRoot
- boolean isDirty = false
+ boolean isDirty()
+ void setIsDirty(boolean isDirty)
}

class DataPackage {
+ void add(AbstractObject obj)
+ boolean contains(Identifier id)
+ AbstractObject get(Identifier id)
+ ResourceMap getMap()
+ Map<Identifier, List<Identifier>> getMetadataMap()
+ Set<Identifier> identifiers()
+ void insertRelationship(Identifier metadataId, List<Identifier>dataIDList)
+ void remove(Identifier id)
+ String serialize()
}

abstract AbstractScienceMetadata {
- Document doc
- boolean isDirty = false
+ abstract void load(Identifier identifier) throws Exception
+ abstract OutputStream serialize() throws Exception
+ boolean isDirty()
+ void setIsDirty(boolean isDirty)
}


class DataStoreController {
+ AbstractObject read(Identifier pid, DataStore store) throws Exception
+ Identifier save(DataPackage DataPackage, DataStore[] stores) throws Exception
+ void delete(DataPackage DataPackage, DataStore[] stores) throws Exception
}

class DataStore {
+ OutputStream get(Identifier id) throws Exception;
+ SystemMetadata getSystemMetadata(Identifier id) throws Exception;
+ void create(Identifier id, InputStream data, SystemMetadata systemMetadata) throws Exception;
+ void delete(Identifier identifier) throws Exception
+ void update(Identifier previousId, Identifier newId, InputStream data, SystemMetadata systemMetadata) throws Exception
+ void OutputStream search(InputStream query, String queryType) throws Exception
}

class FileSystemDataStore {
- HashMap<Identifier, List<File>> fileIDMap
+ OutputStream getCache(Identifier id) throws Exception
+ SystemMetadata getCacheSystemMetadata(Identifier id) throws Exception
+ void createCache(Identifier id, InputStream data, SystemMetadata systemMetadata) throws Exception
+ void deleteCache(Identifier identifier) throws Exception
+ void updateCache(Identifier previousId, Identifier newId, InputStream data, SystemMetadata systemMetadata) throws Exception
}

class MemoryDataStore {

}

class DataONEDataStore {
- MNode activeMNode;
- MNode[] mNodeList;
+ MNode getActiveMNode()
+ void setActiveMNode(MNode activeMNode)
+ boolean isMNodeAvailable(MNode node)
}

D1Object <|-- Entity
D1Object <|-- DataPackage
D1Object "*" o-- "*" DataPackage
D1Object <|-- AbstractScienceMetadata

D1Object "1" o- "1" DataStoreController
DataStoreController "1" o-- "*" DataStore

D1Object "1" o-- "*" DataStore
DataStore <|-- FileSystemDataStore
DataStore <|-- MemoryDataStore
DataStore <|-- DataONEDataStore

@enduml