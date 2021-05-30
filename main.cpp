#include <iostream>
#include <string>
#include <fstream>

//stolen from https://rosettacode.org/wiki/Get_system_command_output#C.2B.2B
std::string execute(const std::string& command) {
	system((command + " > temp.txt").c_str());
	std::ifstream ifs("temp.txt");
	std::string ret{ std::istreambuf_iterator<char>(ifs), std::istreambuf_iterator<char>() };
	ifs.close(); // must close the inout stream so the file can be cleaned up
	if (std::remove("temp.txt") != 0) {
		perror("Error deleting temporary file");
	}
	return ret;
}

int main(int argc, char *argv[])
{
	int usewhichnc = 999;
	if(execute("whereis nc").length() > 3) {
		usewhichnc = 0;
	}else{
		if(execute("where ncat").length() > 5) {
			usewhichnc = 1;
		}else{
			if(execute("where netcat").length() > 7){
				usewhichnc = 2;
			}
		}
	}
	if(usewhichnc == 999){
		std::cout << "No netcat found. ";
	}
	std::cout << "debug: ";
	std::cout << usewhichnc << " ";
	std::string nclookup[3] = {"nc", "ncat", "netcat"};
	std::string ncnum = nclookup[usewhichnc];
	std::cout << ncnum << " ";
	if( argc >= 2 ) {
		std::cout << argc << "\n";
		std::string arg1 = argv[1];
		if ((arg1 == "-h") || (arg1 == "--help") || (arg1 == "Help") || (arg1 == "help")){
			std::cout << "Help command used\n";
			std::cout << "Usage: \n" << "   Send a file: " << argv[0] << " send file.txt secret-code\n" << "   Receive a file: " << argv[0] << " receive\n";
		}
		else if((arg1 == "receive") || (arg1 == "Receive")){
			std::cout << "Receive command used\n";
			std::string localip = execute("hostname -i");
			if(localip.length() >= 10){
				if (localip.find("192.168.0.") != std::string::npos) {
					std::cout << "Found local ip begins with 192.168.0.\n";
					localip.erase(0,10);
				}
			}
			if(argc == 2){
				std::cout << "Use command on sender computer: " << argv[0] << " send file.txt " << localip;
				std::string rcmd = ncnum + " -l -p 1234 > out.file";
				char* rcommand = const_cast<char*>(rcmd.c_str());
				system(rcommand);
			}
		}
		else if((arg1 == "send") || (arg1 == "Send")){
			if(argc==4){
				std::string arg2 = argv[2];
				std::string arg3 = argv[3];
				if(arg3.length() <= 3){
					arg3 = "192.168.0." + arg3;
				}
				std::string cmd = ncnum + " -w 3 " + arg3 + " 1234 < " + arg2;
				char* command = const_cast<char*>(cmd.c_str());
				std::cout << "Send command used with code " << arg2 << " " << arg3 << "\n";
				std::cout << command << "\n";
				system(command);
			}
			else if(argc < 4){
				std::cout << "Not enough arguments used for send command\n";
			}
			else{
				std::cout << "Too many arguments used for send command\n";
			}
		}
	}
	else{
		std::cout << "Please give arguments\n";
	}
	return 0;
}
