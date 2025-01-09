from collections import defaultdict
import csv

class FlowLogParser:
    def __init__(self):
        self.tag_mappings = {}
        self.tag_counts = defaultdict(int)
        self.port_protocol_counts = defaultdict(int)
    
    def load_lookup_table(self, lookup_file):
        with open(lookup_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = (row['dstport'], row['protocol'].lower())
                self.tag_mappings[key] = row['tag']
    
    def process_flow_logs(self, log_file):
        with open(log_file, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 14 or parts[0] != '2':  # Version 2 check
                    continue
                    
                dstport = parts[6]
                protocol = 'tcp' if parts[7] == '6' else 'udp'
                
                # Count port/protocol combinations
                self.port_protocol_counts[(dstport, protocol)] += 1
                
                # Match and count tags
                key = (dstport, protocol)
                tag = self.tag_mappings.get(key, 'Untagged')
                self.tag_counts[tag] += 1
    
    def write_results(self, output_file):
        with open(output_file, 'w') as f:
            # Write tag counts
            f.write("Tag Counts:\n")
            f.write("Tag,Count\n")
            for tag, count in self.tag_counts.items():
                f.write(f"{tag},{count}\n")
            
            # Write port/protocol counts
            f.write("\nPort/Protocol Combination Counts:\n")
            f.write("Port,Protocol,Count\n")
            for (port, protocol), count in self.port_protocol_counts.items():
                f.write(f"{port},{protocol},{count}\n")

def main():
    parser = FlowLogParser()
    parser.load_lookup_table('lookup.csv')
    parser.process_flow_logs('flow_logs.txt')
    parser.write_results('output.csv')

if __name__ == "__main__":
    main()

