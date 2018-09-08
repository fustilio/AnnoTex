require 'sinatra'
require 'pry'

include FileUtils::Verbose

get '/' do
	erb :index
end

post '/upload' do
	#binding.pry
    tempfile = params[:file][:tempfile] 
    filename = params[:file][:filename] 
    cp(tempfile.path, "out/#{filename}")
    result = `python main.py #{filename}`
    redirect "/out/tempLatex.pdf"
end
