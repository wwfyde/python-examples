def main():
    print("Hello from simple-qdrant-app!")
    from qdrant_client import QdrantClient

    qdrant = QdrantClient(
        ":memory:"
    )  # Create in-memory Qdrant instance, for testing, CI/CD
    # OR
    # client = QdrantClient(
    #     path="path/to/db"
    # )  # Persists changes to disk, fast prototyping
    qdrant.add()


if __name__ == "__main__":
    main()
