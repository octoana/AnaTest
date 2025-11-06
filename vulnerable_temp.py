from tempfile import mktemp

def write_results(results):
    filename = mktemp()
    with open(filename, "w+") as f:
        f.write(results)
    print("Results written to", filename)

if __name__ == "__main__":
    # Example usage for testing
    sample_data = "Test results: All tests passed\nStatus: OK"
    write_results(sample_data)
